import os

from ianswer.common import IAnswerObject
from ianswer.common.exceptions import ContentReadException
from ianswer.content.content import ContentCollection, ContentLeaf, Content
from ianswer.reader.support import ParserBuilder, SUPPORTED_EXTENSIONS


class Reader(IAnswerObject):
    """ Interface used to read files """

    def read(self, path_to_folder: str) -> Content:
        return self._read(path_to_folder)

    def _read(self, path_to_folder: str) -> Content:
        return _DirectoryParser().parseDirectory(path_to_folder)
        # return ReaderTxt().read(path_to_folder)


class _DirectoryParser(IAnswerObject):
    def parseDirectory(self, path_to_folder: str, tag: str = 'root') -> ContentCollection:
        dir_contents = os.listdir(path_to_folder)

        file_names = sorted([x for x in dir_contents if x.split('.')[-1] in SUPPORTED_EXTENSIONS],
                            reverse=False)
        directory_names = sorted([x for x in dir_contents if os.path.isdir(os.path.join(path_to_folder, x))],
                                 reverse=False)

        file_paths = [os.path.join(path_to_folder, file) for file in file_names]
        directory_paths = [os.path.join(path_to_folder, directory) for directory in directory_names]

        # Create tree root
        collection = ContentCollection(tag=tag)

        # Collect directories
        for directory_path, directory_name in zip(directory_paths, directory_names):
            dir_collection = self.parseDirectory(directory_path, tag=directory_name)
            collection.add(content=dir_collection)

        # Collect files
        for file_path, file_name in zip(file_paths, file_names):
            try:
                file_leaf = _File.parse(file_path, tag=file_name)
                collection.add(content=file_leaf)
            except ContentReadException as e:
                self.error(f"Could not read '{file_path}'")
        return collection


class _File(IAnswerObject):
    @staticmethod
    def parse(path_to_file: str, tag: str) -> ContentLeaf:
        ext = path_to_file.split('.')[-1]
        parser = ParserBuilder.getParser(ext)
        return parser.parseFile(path_to_file, tag)
