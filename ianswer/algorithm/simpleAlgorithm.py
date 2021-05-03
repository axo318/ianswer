from typing import List
from sklearn.metrics.pairwise import cosine_similarity

from ianswer.algorithm import Algorithm
from ianswer.common import IndexedData, Result
from ianswer.content.content import Content


class SimpleAlgorithm(Algorithm):
    """ Simplest answer finding algorithm. """

    def _index(self, content: Content):
        leaves = content.getLeaves()
        texts = [leaf.processed_data for leaf in leaves]
        embeddings = self._embedder.embedTexts(texts)

        for i in range(len(leaves)):
            leaves[i].indexed_data = IndexedData(embeddings[i])

    def _getResults(self, question: str, content: Content, top_n: int) -> List[Result]:
        # Embed question into a 2d array
        q = self._embedder.embedTexts([question])

        # Retrieve indexed embeddings from the leaves of the content
        leaves = content.getLeaves()
        excerpt_embeddings = [leaf.indexed_data.data for leaf in leaves]
        scores = cosine_similarity(q, excerpt_embeddings)[0]

        # Sort scores
        leaf_scores = zip(leaves, scores)
        sorted_leaf_scores = sorted(leaf_scores, key=lambda tup: tup[1], reverse=True)

        # Construct result objects for the top_n scores
        results = list()
        for leaf, score in sorted_leaf_scores[:top_n]:
            results.append(Result(title=leaf.getTitle(), text=leaf.getText(), score=score))
        return results
