from typing import List
from sklearn.metrics.pairwise import cosine_similarity

from ianswer.common import IAnswerObject, Result, IndexedData
from ianswer.content.content import Content
from ianswer.embedder.embedder import Embedder


class Algorithm(IAnswerObject):
    """ Abstract Algorithm class. Implement it by subclassing """

    # PUBLIC CALLS
    def index(self, content: Content):
        """ Indexes content tree for better performance

        :param content: Content tree to be indexed
        :return:
        """
        self.info("Indexing content tree...")
        self._index(content)

    def getResults(self, question: str, content: Content, top_n: int = 3) -> List[Result]:
        """ Retrieves the #top_n most likely answers to the given question

        :param question: processed question string
        :param content: indexed Content tree
        :param top_n: number of results to return
        :return:
        """
        self.info(f"Fetching answers to: '{question}'")
        return self._getResults(question, content, top_n)

    # PRIVATE CALLS
    def _index(self, content: Content):
        """ Abstract call to be implemented by subclasses of QAAlgorithm

        :param content: Content tree to be indexed
        :return:
        """
        pass

    def _getResults(self, question: str, content: Content, top_n: int) -> List[Result]:
        """ Abstract call to be implemented by subclasses of QAAlgorithm

        :param question: processed question string
        :param content: indexed Content tree
        :param top_n: number of results to return
        :return:
        """
        pass


class SimpleAlgorithm(Algorithm):
    def __init__(self, embedder: Embedder):
        """ Simplest answer finding algorithm.

        Embeds the whole text in each content leaf and directly compares it against input
        answer using cosine similarity.

        :param embedder: Embedder object to use for text embeddings
        """
        self._embedder = embedder

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


