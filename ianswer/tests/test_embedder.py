import unittest
import os
from ianswer.content.content import ContentCollection
from ianswer.embedder.embedder import GoogleEncoder
from ianswer.processor.segmenter import SimpleSegmenter
from ianswer.reader.reader import ReaderTxt


test_folder = 'test_data'
file_path = os.path.dirname(os.path.realpath(__file__))
path_to_folder = os.path.join(file_path, test_folder)


class EmbedderTestCase(unittest.TestCase):

    def test_GoogleEncoder(self):
        collection1 = ReaderTxt().read(path_to_folder=path_to_folder)
        collection1.tag = "collection1"
        collection2 = ReaderTxt().read(path_to_folder=path_to_folder)
        collection2.tag = "collection2"
        collection = ContentCollection()
        collection.add(collection1)
        collection.add(collection2)
        print('Before segmenting...')
        print(collection)

        seg = SimpleSegmenter(tag='Paragraph')
        seg.actOnContent(collection[0])

        emb = GoogleEncoder()
        emb.initialize()
        for i, leaf in enumerate(collection.getLeaves()):
            print(i)
            print(emb.embedText(leaf.getText()))


