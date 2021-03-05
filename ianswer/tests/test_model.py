import unittest

from ianswer.algorithm.algorithm import SimpleAlgorithm
from ianswer.embedder.embedder import GoogleEncoder
from ianswer.model import IModel
from ianswer.processor.preprocessor import SimplePreprocessor
from ianswer.processor.processor import ProcessPipeline
from ianswer.processor.segmenter import SimpleSegmenter
from ianswer.resources import TEST_DATA_FOLDER
from ianswer.utils import getDefaultModel


class IModelTestCase(unittest.TestCase):

    def test_IModel(self):
        pipeline = [SimpleSegmenter(tag='Paragraph'),
                    SimplePreprocessor()
                    ]
        model = IModel(root_dir=TEST_DATA_FOLDER,
                       process_pipeline=ProcessPipeline(*pipeline),
                       embedder=GoogleEncoder(),
                       algorithm=SimpleAlgorithm())

        model.initialize()
        question = "How do we control the formation of nanometer-scale structures?"
        results = model.answers(question, top_n=5)

        print()
        print(results)

    def test_utils_default(self):
        model = getDefaultModel()
        model.initialize()
        question = "How do we control the formation of nanometer-scale structures?"
        results = model.answers(question, top_n=5)

        print()
        print(results)