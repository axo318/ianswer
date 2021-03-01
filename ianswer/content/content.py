

class Content:
    def __init__(self, tag=None, parent=None):
        """
        :param tag:     Name for content instance
        :param parent:  Parent Content
        """
        self._tag = tag
        self._parent = parent

    def __repr__(self):
        return self.getText()

    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, new_tag):
        self._tag = new_tag

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, new_parent):
        self._parent = new_parent

    def getText(self):
        """Returns the text of all text contained in this Content
        """
        pass


class ContentCollection(Content):
    def __init__(self, collection=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._collection = list() if not collection else collection

    def __iter__(self):
        return (x for x in self.collection)

    def __setitem__(self, i, collection):
        self.collection[i] = collection

    def __getitem__(self, i):
        return self.collection[i]

    @property
    def collection(self):
        return self._collection

    @collection.setter
    def collection(self, new_collection):
        self._collection = new_collection

    def add(self, content: Content) -> None:
        """Adds content to collection

        :param content: new contant to be added
        :type content: Content
        """
        content.parent = self
        self._collection.append(content)

    def getText(self):
        return "".join([c.getText() + "\n" for c in self.collection])


class ContentNode(Content):
    def __init__(self, text=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._text = text

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, new_text):
        self._text = new_text

    def getText(self):
        return self.text
