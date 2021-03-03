from ianswer.common import IAnswerObject
from ianswer.content.content import Content
from ianswer.content.utils import getContentLeaves


class PreProcessor(IAnswerObject):

    def actOnContent(self, content: Content) -> None:
        """ Performs pre-processing on the given content tree.
            This should not change the underlying structure of the tree.
            All processing is performed on the data contained in the leaves.
            The processed data is placed in content.processed_data

        :param content: root of the content tree
        :return:
        """
        for leaf in getContentLeaves(content):
            self._processLeaf(leaf)
        pass

    def _processLeaf(self, content: Content) -> None:
        """ Performs pre-processing on the data of given content leaf

        :param content: content leaf object containing data
        :return:
        """
        pass


class SimplePreprocessor(PreProcessor):
    def _processLeaf(self, content: Content) -> None:
        text = content.text_data
        text = text.strip().replace('\n', '')
        content.processed_data = text
