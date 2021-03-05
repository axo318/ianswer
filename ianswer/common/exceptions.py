

class ContentReadException(Exception):
    def __init__(self, content_name):
        """ Custom Exception for reading content

        :param content_name: Name of content_file
        """
        msg = f"Could not read '{content_name}'"
        super().__init__(msg)


class FatalError(Exception):
    def __init__(self, reason):
        """ Custom Exception for unrecoverable errors

        :param reason: short description of the cause of the exception
        """
        msg = f"{reason}"
        super().__init__(msg)
