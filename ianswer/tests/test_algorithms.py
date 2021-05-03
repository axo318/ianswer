import unittest

from ianswer.algorithm import SimpleAlgorithm
from ianswer.algorithm import RollingWindow
from ianswer.embedder.embedder import GoogleEncoder
from ianswer.model import IModel
from ianswer.processor.preprocessor import SimpleCleanPreprocessor
from ianswer.processor.processor import ProcessPipeline
from ianswer.processor.segmenter import NewLineSegmenter
from ianswer.resources import TEST_DATA_FOLDER


class IModelTestCase(unittest.TestCase):

    def test_SimpleAlgorithm(self):
        pipeline = [NewLineSegmenter(tag='Paragraph'),
                    SimpleCleanPreprocessor()
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

    def test_RollingWindow(self):
        pipeline = [NewLineSegmenter(tag='Paragraph'),
                    SimpleCleanPreprocessor()
                    ]
        model = IModel(root_dir=TEST_DATA_FOLDER,
                       process_pipeline=ProcessPipeline(*pipeline),
                       embedder=GoogleEncoder(),
                       algorithm=RollingWindow(N=2))

        model.initialize()
        question = "Control the formation of nanometer-scale structures"
        results = model.answers(question, top_n=5)

        print()
        for result in results:

            print(result.prettify())