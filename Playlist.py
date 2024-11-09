class Song:
    def __init__(self, title):
        self.title = title
        self.next = None
        self.prev = None


class Playlist:
    def __init__(self):
        self.current_song = None

    # Add song to the playlist
    def add_song(self, title):
        new_song = Song(title)
        if not self.current_song:
            # If the playlist is empty, initialize it with the first song
            self.current_song = new_song
            self.current_song.next = self.current_song
            self.current_song.prev = self.current_song
        else:
            # Add new song at the end of the list
            last_song = self.current_song.prev
            last_song.next = new_song
            new_song.prev = last_song
            new_song.next = self.current_song
            self.current_song.prev = new_song

    # Play the current song
    def play_current_song(self):
        if not self.current_song:
            print("The playlist is empty.")
        else:
            print(f"Playing: {self.current_song.title}")

    # Go to the next song
    def play_next_song(self):
        if not self.current_song:
            print("The playlist is empty.")
        else:
            self.current_song = self.current_song.next
            self.play_current_song()

    # Go to the previous song
    def play_previous_song(self):
        if not self.current_song:
            print("The playlist is empty.")
        else:
            self.current_song = self.current_song.prev
            self.play_current_song()

    # Remove the current song from the playlist
    def remove_current_song(self):
        if not self.current_song:
            print("The playlist is empty.")
            return

        song_to_remove = self.current_song

        if song_to_remove.next == song_to_remove:  # Only one song in the playlist
            self.current_song = None
        else:
            prev_song = song_to_remove.prev
            next_song = song_to_remove.next

            prev_song.next = next_song
            next_song.prev = prev_song

            self.current_song = next_song

        print(f"Removed: {song_to_remove.title}")
        song_to_remove = None  # Delete the node

    # Display all songs in the playlist
    def display_playlist(self):
        if not self.current_song:
            print("The playlist is empty.")
            return

        song = self.current_song
        print("Playlist:")
        while True:
            print(song.title)
            song = song.next
            if song == self.current_song:
                break
