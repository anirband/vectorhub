"""
    Vector AI's deployed model. The purpose of this model is to 
    allow developers to easily build encodings and see for themselves
    how the embedding works. These models are selected to work out-of-the-box 
    after testing for their success on our end.

    To get access to Vector AI, we need to use 

    Example:

        >>> from vectorhub.text.encoder.vectorai import ViText2Vec
        >>> model = ViText2Vec(username, api_key)
        >>> model.encode("audio_file.wav")

"""
import io
import base64
import requests
from ..base import BaseAudio2Vec
from ....base import catch_vector_errors

class ViAudio2Vec:
    def __init__(self, username, api_key, url=None, collection_name="base"):
        """
            Request for a username and API key from gh.vctr.ai
        """
        self.username = username
        self.api_key = api_key
        if url:
            self.url = url
        else:
            self.url = "https://api.vctr.ai"
        self.collection_name = collection_name
        self._name = "default"
    
    @catch_vector_errors
    def encode(self, audio):
        return requests.get(
            url="{}/collection/encode_audio".format(self.url),
            params={
                "username": self.username,
                "api_key": self.api_key,
                "collection_name": self.collection_name,
                "audio_url": audio,
            },
        ).json()

    @property
    def __name__(self):
        if self._name is None:
            return "vectorai_audio"
        return self._name

    @__name__.setter
    def __name__(self, value):
        self._name = value
