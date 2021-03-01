import unittest, os
from ianswer.reader.reader import ReaderTxt
from ianswer.content.content import ContentCollection

test_folder = 'test_data'
file_path = os.path.dirname(os.path.realpath(__file__))
path_to_folder = os.path.join(file_path, test_folder)


class ContentTestCase(unittest.TestCase):

    def test_read_files_from_dir(self):
        print()
        collection1 = ReaderTxt().read(path_to_folder=path_to_folder)
        collection2 = ReaderTxt().read(path_to_folder=path_to_folder)
        collection = ContentCollection()
        collection.add(collection1)
        collection.add(collection2)
        print(collection)
        print()
