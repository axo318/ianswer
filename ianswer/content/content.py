from typing import List, Union

from ianswer.common import IAnswerObject, IndexedData


class Content(IAnswerObject):
    def __init__(self,
                 tag: str = "",
                 parent: 'Content' = None,
                 index: int = 0,
                 collection: list = None,
                 text_data: str = None,
                 processed_data: str = None,
                 indexed_data: IndexedData = None):
        """ Tree structure for holding text information

        Tree nodes must always be of subclass ContentCollection
        Tree leaves must always be of subclass ContentLeaf

        :param tag: name of the current Content (root for tree root)
        :param parent: parent content instance of current object (None for root)
        :param index: position of current object in parent
        :param collection: list containing the children of current Content (if node)
        :param text_data: text data contained in the current Content (if leaf)
        :param processed_data: processed data
        :param indexed_data: Algorithm specific storage
        """
        self._tag = tag
        self._parent = parent
        self._index = index
        self._collection = collection
        self._text_data = text_data
        self._processed_data = processed_data
        self._indexed_data = indexed_data

    def __iter__(self):
        if self._collection:
            return (x for x in self.collection)
        return ()

    def __setitem__(self, i, collection):
        if self._collection:
            self.collection[i] = collection

    def __getitem__(self, i) -> Union['Content', None]:
        if self._collection:
            return self.collection[i]
        return None

    # public calls
    def getRepr(self) -> str:
        """ Returns printable string representing the current object

        :return: string representation
        """
        return f"{self.__class__.__name__}(tag= {self._tag})"

    def getLeaves(self) -> List['ContentLeaf']:
        """ Creates a list of leaves using the input content as a tree root
            Left side first

        :return: list containing leaf objects (ContentLeaf)
        """
        stack = list()

        def constructStack(c: Content):
            if c.isLeaf():
                stack.append(c)
                return
            for child in c.collection:
                constructStack(child)

        constructStack(self)
        return stack

    def getRoot(self) -> 'Content':
        """ Returns the tree root which contains the current object

        :return: root of this content's tree
        """
        root = self
        while root.parent:
            root = root.parent
        return root

    def getTitle(self) -> str:
        """ Returns the title of the current Content.

        The title is the path from the tree root to the current content

        :return:
        """
        title_contents = list()
        temp = self
        while temp:
            title_contents.append(temp.tag)
            temp = temp.parent
        return '/'.join(title_contents[::-1])

    def replace(self, new: 'Content'):
        """ Replaces the old content subtree with the new one

        :param new: new Content subtree
        :return:
        """
        parent = self.parent
        index = self.index

        new.parent = parent
        new.index = index

        if parent:
            parent[index] = new

        del self

    def isLeaf(self) -> bool:
        """Determines whether the current object instance is a leaf or a collection"""
        pass

    def getText(self) -> str:
        """Returns all text contained in this Content and in any possible children
        """
        pass

    # getter and Setter properties
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
    def index(self, new_index: int):
        self._index = new_index

    @property
    def indexed_data(self) -> IndexedData:
        return self._indexed_data

    @indexed_data.setter
    def indexed_data(self, new_indexed_data: IndexedData):
        self._indexed_data = new_indexed_data


class ContentCollection(Content):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.collection = list() if not self.collection else self.collection

    def __repr__(self):
        s = self.getRepr() + ' [' + '\n'
        s += '\n'.join(['-> '+c.getRepr() for c in self.collection]).strip()
        s += '\n' + ']'
        return s

    # public calls
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


class ContentLeaf(Content):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text_data = self.text_data if self.text_data else ""

    def __repr__(self):
        s = self.getRepr() + ' [' + '\n'
        s += self.getText().strip()
        s += '\n' + ']'
        return s

    # public calls
    def isLeaf(self):
        return True

    def getText(self):
        return self.text_data
