import datetime
from textwrap import wrap


# UTILS
def getTimestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d T %H:%M:%S.%f")[:-3]


# CLASSES
class IAnswerObject:
    """ Common base class for all class definitions in ianswer """
    def __repr__(self):
        return f"{self.__class__.__name__}()"

    def info(self, msg):
        self._log(self._constructLog(msg, level="INFO"))

    def error(self, msg):
        self._log(self._constructLog(msg, level="ERROR"))

    def _constructLog(self, msg, level="DEBUG") -> str:
        timestamp = getTimestamp()
        class_name = self.__class__.__name__
        return f"[{timestamp}] {class_name} {level}: {msg}"

    def _log(self, log):
        print(log)


class IndexedData:
    def __init__(self, data):
        """ Holder class that can hold arbitrary data """
        self._data = data

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
        self._data = new_data


class Result:
    def __init__(self,
                 title: str,
                 text: str,
                 score: float,
                 answer_loc: tuple = None):
        """ Class which holds a question result

        :param title: title of the text excerpt
        :param text: text excerpt
        :param answer_loc: tuple containing the start and end indexes of the answer inside the excerpt
        """
        self._title = title
        self._text = text
        self._score = score
        self._answer_loc = answer_loc

    def __repr__(self):
        score = "{:.4f}".format(self._score)
        s = f"Result('{self._title}', score={score}) [\n"

        paragraph = "\n".join(wrap(self._text))
        s += f"{paragraph}\n]"
        return s

    def prettify(self, answer_color='\033[92m'):
        score = "{:.4f}".format(self._score)
        s = f"Result('{self._title}', score={score}) [\n"

        if self._answer_loc is not None:
            HIGHLIGHT = answer_color
            RESET = '\033[0m'

            text = self._text
            b = self._answer_loc[0]
            e = self._answer_loc[1]

            new_text = text[:b] + HIGHLIGHT + text[b:e+1] + RESET + text[e+1:]
            paragraph = "\n".join(wrap(new_text))
        else:
            paragraph = "\n".join(wrap(self._text))

        s += f"{paragraph}\n]"
        return s

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, new_title: str):
        self._title = new_title

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, new_text: str):
        self._text = new_text

    @property
    def score(self) -> float:
        return self._score

    @score.setter
    def score(self, new_score: float):
        self._score = new_score

    @property
    def answer_loc(self) -> tuple:
        return self._answer_loc

    @answer_loc.setter
    def answer_loc(self, new_answer_loc: tuple):
        self._answer_loc = new_answer_loc
