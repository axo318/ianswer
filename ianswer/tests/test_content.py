import unittest
import os
from ianswer.content.content import ContentCollection
from ianswer.content.utils import getContentLeaves
from ianswer.reader.reader import ReaderTxt


test_folder = 'test_data'
file_path = os.path.dirname(os.path.realpath(__file__))
path_to_folder = os.path.join(file_path, test_folder)


class ContentTestCase(unittest.TestCase):

    def test_content_is_iterable(self):
        list_ = list(range(3))
        content_ = ContentCollection(collection=list_)
        for i in range(len(content_.collection)):
            self.assertEqual(list_[i], content_[i])
    
    def test_contentCollection_is_iterable_range(self):
        list_ = list(range(3))
        content_ = ContentCollection(collection=list_)
        self.assertEqual(list_[:2], content_[:2])

    def test_contentUtils_getContentLeaves(self):
        collection1 = ReaderTxt().read(path_to_folder=path_to_folder)
        collection2 = ReaderTxt().read(path_to_folder=path_to_folder)
        collection = ContentCollection()
        collection.add(collection1)
        collection.add(collection2)

        leaves = getContentLeaves(collection)
        print(f"Number of leaves: {len(leaves)}")
        for leaf in leaves:
            print(leaf)
