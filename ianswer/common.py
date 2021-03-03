

class IAnswerObject:
    def __repr__(self):
        return f"{self.__class__.__name__}()"

    def info(self, msg):
        pass

    def error(self, msg):
        pass
