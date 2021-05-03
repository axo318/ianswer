from typing import List

from ianswer.common import IAnswerObject, Result
from ianswer.content.content import Content
from ianswer.embedder.embedder import Embedder


class Algorithm(IAnswerObject):
    def __init__(self):
        """ Abstract Algorithm class. Implement it by subclassing """
        self._embedder: Embedder = None

    # PUBLIC CALLS
    def setEmbedder(self, embedder: Embedder):
        """ Sets embedder implementation for use with this algorithm.

        This must be called before indexing or getting results.

        :param embedder:
        :return:
        """
        self._embedder = embedder

    def index(self, content: Content):
        """ Indexes content tree for better performance

        :param content: Content tree to be indexed
        :return:
        """
        self.info("Indexing content tree...")
        self._index(content)

    def getResults(self, question: str, content: Content, top_n: int) -> List[Result]:
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
