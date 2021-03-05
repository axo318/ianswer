import os
from typing import List

import numpy as np
import tensorflow_hub as hub

from ianswer.common import IAnswerObject
from ianswer.common.exceptions import FatalError
from ianswer.resources import RESOURCE_FOLDER

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'    # Silence tensorflow debug info


class Embedder(IAnswerObject):
    """ Abstract Embedder class defining interface for embedder implementations.

    It must be initialized before it can embed input texts.
    """

    # PUBLIC CALLS
    def initialize(self) -> None:
        """ Public call for initializing embedder from storage """
        self.info("Initializing...")
        self._initialize()

    def embedText(self, text: str) -> np.ndarray:
        """ Public call for embedding a text input

        :param text: text string to be embedded
        :return: 1D embedding vector
        """
        list_embeddings = self._embed([text])
        return list_embeddings[0]

    def embedTexts(self, texts: List[str]) -> np.ndarray:
        """ Public call for embedding a list of text inputs

        :param texts: list containing different texts to be embedded
        :return: 2D array containing all embedding vectors
        """
        return self._embed(texts)

    # PRIVATE CALLS
    def _initialize(self) -> None:
        """ Private call to be defined by Embedder implementations
            This should initialize self.embedder_engine
        """
        pass

    def _embed(self, texts: List[str]) -> np.ndarray:
        """ Private call to be defined by Embedder implementations
            It must return an embedding vector of the text input

        :param texts: list containing different texts to be embedded
        :return: 2D array containing all embedding vectors
        """
        pass


class GoogleEncoder(Embedder):
    def __init__(self):
        """ Embedder implementation using Google Sentence Encoder """
        self._model_dir_name = "universal-sentence-encoder_4"
        self.encoder_path = os.path.join(RESOURCE_FOLDER, self._model_dir_name)
        self.model_embed = None

    def _initialize(self):
        if os.path.exists(self.encoder_path):
            self.model_embed = hub.load(self.encoder_path)
        else:
            self.error("Cannot load google sentence encoder from storage.")
            raise FatalError(f"'{self._model_dir_name}' does not exist in resources")

    def _embed(self, texts):
        return self.model_embed(texts).numpy()
