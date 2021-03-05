import unittest
import os

from ianswer.algorithm.algorithm import SimpleAlgorithm
from ianswer.embedder.embedder import GoogleEncoder
from ianswer.processor.preprocessor import SimpleCleanPreprocessor
from ianswer.processor.segmenter import NewLineSegmenter
from ianswer.reader.reader import ReaderTxt


test_folder = 'test_data'
file_path = os.path.dirname(os.path.realpath(__file__))
path_to_folder = os.path.join(file_path, test_folder)


class AlgorithmTestCase(unittest.TestCase):

    def test_SimpleAlgorithm(self):
        collection = ReaderTxt().read(path_to_folder=path_to_folder)
        print('Before segmenting...')
        print(collection)

        seg = NewLineSegmenter(tag='Paragraph')
        seg.actOnContent(collection)

        preprocessor = SimpleCleanPreprocessor()
        preprocessor.actOnContent(collection)

        emb = GoogleEncoder()
        emb.initialize()
        alg = SimpleAlgorithm()
        alg.setEmbedder(emb)
        alg.index(collection)

        results = alg.getResults("Where did the Top-Down approach originate?", collection)
        for result in results:
            print(result)

