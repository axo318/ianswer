import unittest
import os
from ianswer.content.content import ContentCollection
from ianswer.content.utils import getContentLeaves
from ianswer.reader.reader import ReaderTxt
from ianswer.processor.preprocessor import SimplePreprocessor


test_folder = 'test_data'
file_path = os.path.dirname(os.path.realpath(__file__))
path_to_folder = os.path.join(file_path, test_folder)


class PreprocessorTestCase(unittest.TestCase):

    def test_SimplePreprocessor(self):
        collection1 = ReaderTxt().read(path_to_folder=path_to_folder)
        collection2 = ReaderTxt().read(path_to_folder=path_to_folder)
        collection = ContentCollection()
        collection.add(collection1)
        collection.add(collection2)

        pre = SimplePreprocessor()
        pre.actOnContent(collection)

        leaves = getContentLeaves(collection)
        print(f"Number of leaves: {len(leaves)}")
        for leaf in leaves:
            print(leaf.processed_data)
