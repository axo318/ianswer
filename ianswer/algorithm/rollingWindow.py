from typing import List
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import sent_tokenize
import numpy as np

from ianswer.algorithm import Algorithm
from ianswer.common import IndexedData, Result
from ianswer.content.content import Content


class RollingWindow(Algorithm):

    def __init__(self, N: int = 3):
        """ Rolling Window based answer finding algorithm.

        :param N: Number of sentences to include in the rolling window
        """
        super().__init__()
        self.N = N if N > 0 else 1

    def _index(self, content: Content):
        leaves = content.getLeaves()

        for leaf in leaves:
            text = leaf.processed_data
            orig_text = leaf.getText()
            sentences = sent_tokenize(text)
            orig_sentences = sent_tokenize(orig_text)

            # If it is short embed the whole text
            if len(sentences) < self.N:
                texts = [' '.join(sentences)]
                orig_texts = [' '.join(orig_sentences)]
                locations = [tuple([0, len(orig_texts[0])])]
            else:
                texts = [' '.join(sentences[i:i+self.N]) for i in range(len(sentences) - self.N + 1)]
                orig_texts = [' '.join(orig_sentences[i:i+self.N]) for i in range(len(orig_sentences) - self.N + 1)]
                locations = []
                for i, t in enumerate(orig_texts):
                    start = len(" ".join(orig_sentences[:i]))
                    end = start + len(t)
                    locations.append(tuple([start, end]))

            # Calculate embeddings
            embeddings = self._embedder.embedTexts(texts)

            # Calculate embedding text positions
            # locations = []
            # for t in range(len(orig_texts)):
            #     start = len(' '.join(orig_texts[:t]))
            #     end = len(' '.join(orig_texts[:t+1]))
            #     locations.append(tuple([start, end]))

            embeddings_data = list(zip(embeddings, locations))
            leaf.indexed_data = IndexedData(embeddings_data)

    def _getResults(self, question: str, content: Content, top_n: int) -> List[Result]:
        # Embed question into a 2d array
        q = self._embedder.embedTexts([question])

        # Retrieve indexed embeddings from the leaves of the content
        leaves = content.getLeaves()
        excerpt_embedding_data = [leaf.indexed_data.data for leaf in leaves]

        # Get all scores for every rolling window
        rolling_scores = []
        for i in range(len(excerpt_embedding_data)):
            cur_embeddings = [element[0] for element in excerpt_embedding_data[i]]
            locations = [element[1] for element in excerpt_embedding_data[i]]

            scores = cosine_similarity(q, cur_embeddings)[0]
            scores_with_locations = list(zip(scores, locations))

            rolling_scores.append(scores_with_locations)

        # rolling_scores = [cosine_similarity(q, excerpt_embedding_data[i][0])[0] for i in range(len(excerpt_embedding_data))]

        # Select maximum score from each window list and its index location in the text
        max_scores = []
        for i in range(len(rolling_scores)):
            leaf_scores = [element[0] for element in rolling_scores[i]]
            max_ind = np.argmax(leaf_scores)

            max_score = rolling_scores[i][max_ind]
            max_scores.append(max_score)

        # Sort scores
        leaf_scores = zip(leaves, max_scores)
        sorted_leaf_scores = sorted(leaf_scores, key=lambda tup: tup[1][0], reverse=True)

        # Construct result objects for the top_n scores
        results = list()
        for leaf, score in sorted_leaf_scores[:top_n]:
            results.append(Result(title=leaf.getTitle(), text=leaf.processed_data, score=score[0], answer_loc=score[1]))
        return results
