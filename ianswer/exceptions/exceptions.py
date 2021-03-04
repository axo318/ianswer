

class ContentReadException(Exception):
    """Custom Exception for reading content"""
    def __init__(self, content_name):
        """
        :param content_name: Name of content_file
        """
        msg = f"Could not read '{content_name}'"
        super().__init__(msg)