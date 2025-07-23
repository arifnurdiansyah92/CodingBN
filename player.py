import time

class AudioTrack:
    """
    The base class for any audio track in the music player.
    Encapsulates the core details of a track.
    """
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration # in seconds
        # Encapsulation: Play count is private and managed internally.
        self.__play_count = 0

    def get_play_count(self):
        """A public method to safely access the private play count."""
        return self.__play_count

    def play(self):
        """
        Polymorphism: This is the base play method.
        It increments the play count.
        """
        self.__play_count += 1
        print(f"Playing '{self.title}' by {self.artist}...", end="")
        # Simulate playing the track
        time.sleep(1) 
        print(" Done.")

class Song(AudioTrack):
    """
    Inheritance: A specific type of AudioTrack for songs.
    """
    def __init__(self, title, artist, duration, album):
        # Call the parent's constructor
        super().__init__(title, artist, duration)
        self.album = album

    def play(self):
        """
        Polymorphism: Overrides the parent method to provide a
        song-specific message.
        """
        print(f"Playing song: '{self.title}' from the album '{self.album}'...")
        # Call the parent's play method to handle the core logic (incrementing count)
        super().play()

class Podcast(AudioTrack):
    """
    Inheritance: A specific type of AudioTrack for podcasts.
    """
    def __init__(self, title, artist, duration, guest):
        super().__init__(title, artist, duration)
        self.guest = guest

    def play(self):
        """
        Polymorphism: Overrides the parent method to provide a
        podcast-specific message.
        """
        print(f"Playing podcast: '{self.title}' featuring special guest {self.guest}...")
        super().play()

class MusicPlayer:
    """A manager class to hold and manage the playlist."""
    def __init__(self):
        self.playlist = []

    def add_track(self, track):
        """Adds an AudioTrack object to the playlist."""
        if isinstance(track, AudioTrack):
            self.playlist.append(track)
        else:
            print("Error: Only AudioTrack objects can be added.")

    def play_all(self):
        """Plays all tracks in the playlist."""
        print("\n--- Starting Playlist ---")
        if not self.playlist:
            print("Playlist is empty.")
        else:
            for track in self.playlist:
                track.play()
        print("--- Playlist Finished ---\n")

    def show_stats(self):
        """Displays the play count for each track in the playlist."""
        print("\n--- Playlist Statistics ---")
        if not self.playlist:
            print("Playlist is empty.")
        else:
            for track in self.playlist:
                print(f"'{track.title}' - Played {track.get_play_count()} time(s).")
        print("-------------------------\n")

def main():
    """The main function to run the interactive program."""
    player = MusicPlayer()

    # Populate with initial tracks
    player.add_track(Song("Bohemian Rhapsody", "Queen", 355, "A Night at the Opera"))
    player.add_track(Podcast("Tech Today", "The Techie", 1800, "Dr. Eva Core"))
    player.add_track(Song("Stairway to Heaven", "Led Zeppelin", 482, "Led Zeppelin IV"))

    while True:
        print("Digital Music Player")
        print("1. Play all tracks in playlist")
        print("2. Show playlist statistics")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            player.play_all()
        elif choice == '2':
            player.show_stats()
        elif choice == '3':
            print("Shutting down player. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")

main()
