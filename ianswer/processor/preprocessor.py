from ianswer.content.content import Content
from ianswer.processor.processor import Processor


class PreProcessor(Processor):

    def _actOnContent(self, content: Content) -> None:
        """ Performs pre-processing on the given content tree.
            This should not change the underlying structure of the tree.
            All processing is performed on the data contained in the leaves.
            The processed data is placed in content.processed_data

        :param content: root of the content tree
        :return:
        """
        for leaf in content.getLeaves():
            self._processLeaf(leaf)

    def _processLeaf(self, content: Content) -> None:
        """ Performs pre-processing on the data of given content leaf

        :param content: content leaf object containing data
        :return:
        """
        pass


class SimpleCleanPreprocessor(PreProcessor):
    """ Cleans text from double spaces, newline characters and any trailing characters """
    def _processLeaf(self, content: Content) -> None:
        text = content.text_data
        text = text.strip().replace('\n', '')
        text = " ".join(text.split(' '))
        content.processed_data = text
