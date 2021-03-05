
from ianswer.common import IAnswerObject
from ianswer.reader.utils import Responsibility
from ianswer.common.exceptions import ContentReadException
from ianswer.content.content import ContentLeaf


SUPPORTED_EXTENSIONS = [
    'txt',
]


class ParserBuilder:
    @staticmethod
    def getParser(extension) -> 'FileParser':
        parser = Responsibility.d[extension]
        return parser()


class FileParser(IAnswerObject):
    def parseFile(self, path_to_file: str, tag: str) -> ContentLeaf:
        return self._parseFile(path_to_file, tag)

    def _parseFile(self, path_to_file: str, tag: str) -> ContentLeaf:
        pass


@Responsibility.register(['txt'])
class TxtFileParser(FileParser):
    def _parseFile(self, path_to_file: str, tag: str) -> ContentLeaf:
        try:
            with open(path_to_file, 'r') as open_file:
                text = open_file.read()
                content = ContentLeaf(tag=tag, text_data=text)
        except Exception as e:
            raise ContentReadException(path_to_file) from e
        return content
