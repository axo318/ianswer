from ianswer.common import IAnswerObject


class Content(IAnswerObject):
    def __init__(self, tag="", parent=None, collection=None, text_data=None, processed_data=None, index=0):
        """
        :param tag:     Name for content instance
        :param parent:  Parent Content
        """
        self._tag = tag
        self._parent = parent
        self._index = index
        self._collection = collection
        self._text_data = text_data
        self._processed_data = processed_data

    @property
    def tag(self) -> str:
        return self._tag

    @tag.setter
    def tag(self, new_tag):
        self._tag = new_tag

    @property
    def parent(self) -> 'Content':
        return self._parent

    @parent.setter
    def parent(self, new_parent):
        self._parent = new_parent

    @property
    def collection(self) -> list:
        return self._collection

    @collection.setter
    def collection(self, new_collection):
        self._collection = new_collection

    @property
    def text_data(self) -> str:
        return self._text_data

    @text_data.setter
    def text_data(self, new_text):
        self._text_data = new_text

    @property
    def processed_data(self) -> str:
        return self._processed_data

    @processed_data.setter
    def processed_data(self, mew_processed_data):
        self._processed_data = mew_processed_data

    @property
    def index(self) -> int:
        return self._index

    @index.setter
    def index(self, new_index):
        self._index = new_index

    def getRepr(self) -> str:
        """ Returns printable string representing the current object

        :return: string representation
        """
        return f"{self.__class__.__name__}(tag = {self._tag})"

    def isLeaf(self) -> bool:
        """Determines whether the current object instance is a leaf or a collection"""
        pass

    def getText(self) -> str:
        """Returns all text contained in this Content and in any possible children
        """
        pass


class ContentCollection(Content):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.collection = list() if not self.collection else self.collection

    def __repr__(self):
        s = self.getRepr() + ' [' + '\n'
        s += '\n'.join([c.getRepr() for c in self.collection]).strip()
        s += '\n' + ']'
        return s

    def __iter__(self):
        return (x for x in self.collection)

    def __setitem__(self, i, collection):
        self.collection[i] = collection

    def __getitem__(self, i):
        return self.collection[i]

    def add(self, content: Content) -> None:
        """Adds content to collection

        :param content: new content to be added
        :type content: Content
        """
        content.parent = self
        content.index = len(self.collection)
        self.collection.append(content)

    def isLeaf(self):
        return False

    def getText(self):
        return "".join([c.getText() + "\n" for c in self.collection])


class ContentNode(Content):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text_data = self.text_data if self.text_data else ""

    def __repr__(self):
        s = self.getRepr() + ' [' + '\n'
        s += self.getText().strip()
        s += '\n' + ']'
        return s

    def isLeaf(self):
        return True

    def getText(self):
        return self.text_data
