import unittest
import os
from ianswer.content.content import ContentCollection
from ianswer.processor.segmenter import NewLineSegmenter
from ianswer.reader.reader import ReaderTxt


test_folder = 'test_data'
file_path = os.path.dirname(os.path.realpath(__file__))
path_to_folder = os.path.join(file_path, test_folder)


class PreprocessorTestCase(unittest.TestCase):

    def test_SimpleSegmenter(self):
        collection1 = ReaderTxt().read(path_to_folder=path_to_folder)
        collection1.tag = "collection1"
        collection2 = ReaderTxt().read(path_to_folder=path_to_folder)
        collection2.tag = "collection2"
        collection = ContentCollection()
        collection.add(collection1)
        collection.add(collection2)
        print('Before segmenting...')
        print(collection)
        print()

        seg = NewLineSegmenter(tag='Paragraph')
        seg.actOnContent(collection[0])
        print('After Segmenting...')
        print(collection)
        print(collection[0])
        print(collection1[0][4])

