from ianswer.common import IAnswerObject
from ianswer.content.content import Content


class Processor(IAnswerObject):
    def actOnContent(self, content: Content) -> None:
        """ Performs processing routines on the given content tree.
        Passes execution implementation to private _actOnContent method, defined in
        implementations of Processor.

        :param content: root of the content tree
        :return:
        """
        self._actOnContent(content)

    def _actOnContent(self, content: Content) -> None:
        pass


class ProcessPipeline(IAnswerObject):
    def __init__(self, *processors: Processor):
        """ Pipeline class for applying multiple processors on a content in series.

        Processors are applied in the order they are when passed in the constructor

        :param processors: arbitrary number of Processor objects
        """
        self._processors = processors

    def actOnContent(self, content: Content) -> None:
        """ Applies the processors passed in the constructor on the input content tree

        :param content: root of Content tree
        :return:
        """
        for processor in self._processors:
            processor.actOnContent(content)
