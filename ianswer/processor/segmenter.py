from ianswer.content.content import Content, ContentCollection, ContentLeaf
from ianswer.processor.processor import Processor


class Segmenter(Processor):
    def __init__(self, tag="segment") -> None:
        """ Instantiates segmenter object with the given tag

        :param tag: depth level of depth segmentation. Can be user-defined string.
                    eg. 'Paragraph', 'Sentence', 'Word' etc
                    This will be the tag given to the newly created content leaves
        """
        self.child_tag = tag

    def _actOnContent(self, content: Content) -> None:
        """ Performs segmenting steps on the leaves of input content tree.
            Changes the underlying structure of the tree.
            The tree's depth will either remain constant or increase.
            Uses and modifies the text_data field of the Content tree.

        :param content: root of the content tree
        :return:
        """
        for leaf in content.getLeaves():
            new_subtree = self._segmentLeaf(leaf)
            leaf.replace(new_subtree)

    def _segmentLeaf(self, content: ContentLeaf) -> ContentCollection:
        """ Segments the input content leaf and returns a new Content object

        :param content: content leaf object containing data
        :return:
        """
        pass


class NewLineSegmenter(Segmenter):
    """ Segments given text for every newline character.
    """
    def _segmentLeaf(self, content: ContentLeaf) -> ContentCollection:
        text = content.getText()

        segments = [x.strip() for x in text.split('\n')]
        segmented_text = [x for x in segments if x]

        content_collection = ContentCollection(tag=content.tag)
        for i, paragraph in enumerate(segmented_text):
            content_collection.add(ContentLeaf(tag=f"{self.child_tag} {i+1}", text_data=paragraph))

        return content_collection
