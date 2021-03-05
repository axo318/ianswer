from ianswer.algorithm.algorithm import SimpleAlgorithm
from ianswer.embedder.embedder import GoogleEncoder
from ianswer.model import IModel
from ianswer.processor.preprocessor import SimpleCleanPreprocessor
from ianswer.processor.processor import ProcessPipeline
from ianswer.processor.segmenter import NewLineSegmenter


def getDefaultModel(path):
    pipeline = [NewLineSegmenter(tag='Paragraph'),
                SimpleCleanPreprocessor()
                ]
    return IModel(root_dir=path,
                  process_pipeline=ProcessPipeline(*pipeline),
                  embedder=GoogleEncoder(),
                  algorithm=SimpleAlgorithm())