"""A video playlist class."""

from typing import Sequence
from .video import Video

class Playlist:
    """A class used to represent a Playlist."""

    def __init__(self, name: str):
        self._name = name
        self._videos = {}

    def set_name(self, name: str):
        self._name = name

    def name(self) -> str:
        return self._name

    def videos(self) -> Sequence[Video]:
        return self._videos

    def add(self, video: Video):
        self._videos[video.video_id] = video

    def remove(self, video):
        del self._videos[video.video_id]

    def clear(self):
        self._videos = {}
