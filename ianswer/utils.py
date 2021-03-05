from ianswer.algorithm.algorithm import SimpleAlgorithm
from ianswer.embedder.embedder import GoogleEncoder
from ianswer.model import IModel
from ianswer.processor.preprocessor import SimplePreprocessor
from ianswer.processor.processor import ProcessPipeline
from ianswer.processor.segmenter import SimpleSegmenter
from ianswer.resources import TEST_DATA_FOLDER


def getDefaultModel():
    pipeline = [SimpleSegmenter(tag='Paragraph'),
                SimplePreprocessor()
                ]
    return IModel(root_dir=TEST_DATA_FOLDER,
                  process_pipeline=ProcessPipeline(*pipeline),
                  embedder=GoogleEncoder(),
                  algorithm=SimpleAlgorithm())