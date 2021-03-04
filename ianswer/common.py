import datetime


# UTILS
def getTimestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d T %H:%M:%S.%f")


# CLASSES
class IAnswerObject:
    """Common base class for all class definitions in ianswer"""
    def __repr__(self):
        return f"{self.__class__.__name__}()"

    def info(self, msg):
        self._log(self._constructLog(msg, level="INFO"))

    def error(self, msg):
        self._log(self._constructLog(msg, level="ERROR"))

    def _constructLog(self, msg, level="DEBUG") -> str:
        timestamp = getTimestamp()
        class_name = self.__class__.__name__
        return f"[{timestamp}] {class_name} {level}: {msg}\n"

    def _log(self, log):
        print(log)
