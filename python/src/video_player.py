"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._paused = False
        self._playing = None
        self._playlists = {}

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        print("Here's a list of all available videos:")
        videos = self._video_library.get_all_videos()
        videos.sort(key=lambda x: x.title)
        for v in videos:
            print(f"{v.parse_video()}")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        new_video = self._video_library.get_video(video_id)
        if not new_video:
            print("Cannot play video: Video does not exist")
        else:
            self._paused = False
            if self._playing:
                print(
                    f"Stopping video: {self._video_library.get_video(self._playing).title}")
            self._playing = video_id
            print(
                f"Playing video: {self._video_library.get_video(self._playing).title}")

    def stop_video(self):
        """Stops the current video."""
        if not self._playing:
            print("Cannot stop video: No video is currently playing")
        else:
            print(
                f"Stopping video: {self._video_library.get_video(self._playing).title}")
            self._playing = None

    def play_random_video(self):
        """Plays a random video from the video library."""

        videos = self._video_library.get_all_videos()
        video = random.choice(videos)
        self.play_video(video.video_id)

    def pause_video(self):
        """Pauses the current video."""

        if not self._playing:
            print("Cannot pause video: No video is currently playing")
        else:
            if (not self._paused):
                print(
                    f"Pausing video: {self._video_library.get_video(self._playing).title}")
                self._paused = True
            else:
                print(
                    f"Video already paused: {self._video_library.get_video(self._playing).title}")

    def continue_video(self):
        """Resumes playing the current video."""

        if not self._playing:
            print("Cannot continue video: No video is currently playing")
        else:
            if not self._paused:
                print("Cannot continue video: Video is not paused")
            else:
                print(
                    f"Continuing video: {self._video_library.get_video(self._playing).title}")
                self._paused = False

    def show_playing(self):
        """Displays video currently playing."""

        if not self._playing:
            print("No video is currently playing")
        else:
            video = self._video_library.get_video(self._playing)
            out = f"Currently playing: {video.parse_video()}"
            if self._paused:
                out += " - PAUSED"
            print(out)

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if not self._playlists.get(playlist_name.lower(), None):
            self._playlists[playlist_name.lower()] = Playlist(playlist_name)
            print(f"Successfully created new playlist: {playlist_name}")
        else:
            print("Cannot create playlist: A playlist with the same name already exists")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        video = self._video_library.get_video(video_id)

        playlist = self._playlists.get(playlist_name.lower())

        if playlist and video:
            if not video_id in playlist.videos():
                playlist.add(video)
                print(f"Added video to {playlist_name}: {video.title}")
            else:
                print(
                    f"Cannot add video to {playlist_name}: Video already added")

        if not playlist:
            print(
                f"Cannot add video to {playlist_name}: Playlist does not exist")

        elif not video:
            print(f"Cannot add video to {playlist_name}: Video does not exist")

    def show_all_playlists(self):
        """Display all playlists."""
        if not len(self._playlists):
            print("No playlists exist yet")
        else:
            print("Showing all playlists:")
            for playlist in sorted(self._playlists.keys()):
                print(f"{self._playlists[playlist].name()}")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist = self._playlists.get(playlist_name.lower())
        if not playlist:
            print(
                f"Cannot show playlist {playlist_name}: Playlist does not exist")
        else:
            print(f"Showing playlist: {playlist_name}")
            videos = playlist.videos()
            if not len(videos):
                print(f"No videos here yet")
            else:
                for key in videos:
                    print(videos[key].parse_video())

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        playlist = self._playlists.get(playlist_name.lower())
        video = self._video_library.get_video(video_id)

        if (playlist):
            if (video):
                videos_list = playlist.videos()
                if video.video_id in videos_list:
                    playlist.remove(video)
                    print(f"Removed video from {playlist_name}: {video.title}")
                else:
                    print(
                        f"Cannot remove video from {playlist_name}: Video is not in playlist")
            else:
                print(
                    f"Cannot remove video from {playlist_name}: Video does not exist")
        else:
            print(
                f"Cannot remove video from {playlist_name}: Playlist does not exist")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist = self._playlists.get(playlist_name.lower())
        if not playlist:
            print(
                f"Cannot clear playlist {playlist_name}: Playlist does not exist")
        else:
            playlist.clear()
            print(f"Successfully removed all videos from {playlist_name}")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist = self._playlists.get(playlist_name)
        if not playlist:
            print(
                f"Cannot delete playlist {playlist_name}: Playlist does not exist")
        else:
            self._playlists.pop(playlist_name)
            print(f"Deleted playlist: {playlist_name}")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        videos = self._video_library.get_all_videos()
        out = []
        for video in videos:
            if search_term.lower() in video.title.lower():
                out.append(video)
        if not out:
            print(f"No search results for {search_term}")
        else:
            print(f"Here are the results for {search_term}:")
            for i in range(len(out)):
                print(f"  {i+1}) {out[i].parse_video()}")
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            inp = input()
            try:
                num = int(inp)
                if (num in range(0, len(out)+1)):
                    self.play_video(out[num - 1].video_id)
            except:
                pass

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        videos = self._video_library.get_all_videos()
        out = []
        for video in videos:
            if video_tag in video.tags:
                out.append(video)
        if not out:
            print(f"No search results for {video_tag}")
        else:
            print(f"Here are the results for {video_tag}:")
            for i in range(len(out)):
                print(f"  {i+1}) {out[i].parse_video()}")
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            inp = input()
            try:
                num = int(inp)
                if (num in range(0, len(out)+1)):
                    self.play_video(out[num - 1].video_id)
            except:
                pass

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
