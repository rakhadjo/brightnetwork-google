"""A video playlist class."""

from typing import Sequence
from .video import Video

class Playlist:
    """A class used to represent a Playlist."""

    def __init__(self, name: str):
        self._name = name
        self._videos = {}

    @property
    def name(self) -> str:
        return self._name

    @property
    def videos(self) -> Sequence[Video]:
        return self._videos

    def add(self, video: Video):
        self._videos[video.video_id] = Video
