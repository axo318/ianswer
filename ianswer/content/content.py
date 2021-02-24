import os


class ContentReadException(Exception):
    """Custom Exception for reading content"""
    def __init__(self, content_name):
        """
        :param content_name: Name of content_file
        """
        msg = f"Could not read '{content_name}'"
        super().__init__(msg)


class Content:
    def __init__(self, tag=None, parent=None):
        """
        :param tag:     Name for content instance
        :param parent:  Parent Content
        """
        self.tag = tag
        self.parent = parent

    def getTag(self):
        return self.tag

    def getParent(self):
        return self.parent


class ContentCollection(Content):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.collection = list()


class ContentNode(Content):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = None


SUPPORTED_EXTENSIONS = ['txt']


def collectContent(path_to_folder):
    file_names = [x for x in os.listdir(path_to_folder) if x.split('.')[-1] in SUPPORTED_EXTENSIONS]
    content_files = [os.path.join(path_to_folder, file) for file in file_names]

    texts = []
    for file in content_files:
        try:
            with open(file, 'r') as open_file:
                text = open_file.read()
                texts.append(text)
        except Exception as e:
            raise ContentReadException(file) from e

    return texts