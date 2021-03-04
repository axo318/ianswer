from typing import Callable

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
