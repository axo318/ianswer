import unittest
from ianswer.content.content import ContentCollection


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