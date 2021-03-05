import unittest
from ianswer.reader.reader import Reader
from ianswer.resources import TEST_DATA_FOLDER


class ContentTestCase(unittest.TestCase):

    def test_read_files_from_dir(self):
        print()
        collection = Reader().read(path_to_folder=TEST_DATA_FOLDER)
        print(collection)
        print(collection[0])
        print()
