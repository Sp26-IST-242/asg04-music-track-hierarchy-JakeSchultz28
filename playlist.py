"""
A collection class that holds MusicTrack objects (Songs and Podcasts).

Design notes:
  • _tracks is kept private (single underscore) and exposed as a *copy*
    through the `tracks` property to protect encapsulation.
  • clear_playlist() uses list.clear() rather than rebinding to None or a new
    list, so the internal object reference stays valid.
  • sort_by_release_year() delegates to list.sort(), which in turn calls
    MusicTrack.__lt__ — the comparison logic defined in Part 3 pays off here.
  • __str__ uses a generator expression with str.join() for a concise
    multi-line string without building an intermediate list manually.
"""

class Playlist:
    
    # Constructor
    def __init__(self):
        self._tracks = []

    # Getter
    @property
    def tracks(self):
        # Returns list of tracks
        return self._tracks.copy()
    
    def add_track(self, track):
        # Adds to track list
        self._tracks.append(track)

    def clear_playlist(self):
        # Clears track list
        self._tracks.clear() 

    def sort_by_release_year(self):
        # Sorts track list by release year
        self._tracks.sort()

    def __str__(self):
        # Prints the full playlist
        return "\n".join(str(track) for track in self._tracks)