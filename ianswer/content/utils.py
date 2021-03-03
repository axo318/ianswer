from ianswer.content.content import Content


def getContentLeaves(content: Content) -> list:
    """ Creates a list of leaves using the input content as a tree root
        Left side first

    :param content: root of the content tree
    :return: list containing leaf objects (ContentNode)
    """
    stack = list()

    def constructStack(c: Content):
        if c.isLeaf():
            stack.append(c)
            return
        for child in c.collection:
            constructStack(child)

    constructStack(content)
    return stack


def getRoot(content: Content) -> Content:
    """ Returns the tree root which contains the current object

    :param content:
    :return:
    """
    root = content
    while content.parent:
        root = content.parent
    return root


