import os

from ianswer.common import IAnswerObject
from ianswer.common.exceptions import ContentReadException
from ianswer.content.content import ContentCollection, ContentLeaf, Content


SUPPORTED_EXTENSIONS = ['txt']


class Reader(IAnswerObject):
    """Interface used to read files"""

    def read(self, path_to_folder: str) -> Content:
        return self._read(path_to_folder)

    # This is temporary
    # !TODO: Add support for recursive directories
    # !TODO: Add support for multiple file types
    def _read(self, path_to_folder: str) -> Content:
        return ReaderTxt().read(path_to_folder)


class ReaderTxt(Reader):
    """Reader Responsible for reading .txt files"""

    def _read(self, path_to_folder):
        """Reads files from folder and returns collection

        :param path_to_folder: path to folder
        :type path_to_folder: str
        :raises ContentReadException: if file can't be read
        :return: ContentCollection containing all the text
        :rtype: Content
        """
        file_names = sorted([x for x in os.listdir(path_to_folder) if x.split('.')[-1] in SUPPORTED_EXTENSIONS], reverse=False)
        content_files = [os.path.join(path_to_folder, file) for file in file_names]
        collection = ContentCollection(tag='root')
        for file, file_name in zip(content_files, file_names):
            try:
                with open(file, 'r') as open_file:
                    text = open_file.read()
                    content = ContentLeaf(tag=file_name, text_data=text)
                    collection.add(content=content)
            except Exception as e:
                raise ContentReadException(file) from e
        return collection
