from ianswer.algorithm.algorithm import Algorithm
from ianswer.common import IAnswerObject
from ianswer.content.content import Content
from ianswer.embedder.embedder import Embedder
from ianswer.processor.processor import ProcessPipeline
from ianswer.reader.reader import Reader


class IModel(IAnswerObject):
    def __init__(self,
                 root_dir: str,
                 process_pipeline: ProcessPipeline,
                 embedder: Embedder,
                 algorithm: Algorithm):
        """ Generic ianswer model.

        The model reads root_dir and saves data inside a Content tree for processing and
        answer retrieving.

        :param root_dir: path to text files containing answer content
        :param process_pipeline: ProcessPipeline object defining preprocessing steps
        :param embedder: Embedder object for text->vector conversion
        :param algorithm: Algorithm to be used for answer finding
        """
        self._root_dir = root_dir
        self._process_pipeline = process_pipeline
        self._embedder = embedder
        self._algorithm = algorithm

        self._content: Content = None

    def initialize(self) -> None:
        """ Initializes model by loading configuration from storage and indexing contents """
        self.info("Initializing...")

        # Construct content Tree
        self._content = Reader().read(self._root_dir)

        # Apply process pipeline
        self._process_pipeline.actOnContent(self._content)

        # Initialize embedder, pass it to the algorithm and index content tree
        self._embedder.initialize()
        self._algorithm.setEmbedder(self._embedder)
        self._algorithm.index(self._content)

    def answers(self, question: str, top_n: int = 3):
        """ Returns the top_n answers to the input question as a list of Result objects

        :param question: string question to be answered
        :param top_n: number of matching results to show
        :return:
        """
        return self._algorithm.getResults(question=question,
                                          content=self._content,
                                          top_n=top_n)

