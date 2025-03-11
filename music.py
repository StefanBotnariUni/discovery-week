import pygame
import random

class Music:
    root = "./src/"

    def __init__(self,
                 bg_volume: float = 1.0,
                 sfx_volume: float = 1.0) -> None:

        """
        Initializes the Music class with separate volume controls.

        :param bg_volume: Volume for background music.
        :param sfx_volume: Volume for sound effects.
        """

        pygame.mixer.init()
        self.bg_volume = bg_volume
        self.sfx_volume = sfx_volume
        pygame.mixer.music.set_volume(self.bg_volume)

        self.background_music = [
            rf"{self.root}/background_music1.mp3",
            rf"{self.root}/background_music2.mp3",
            rf"{self.root}/background_music3.mp3"
        ]
        self.sounds = {}

    def play_background(self) -> None:

        """Plays a random background music track in a loop."""

        pygame.mixer.music.load(random.choice(self.background_music))
        pygame.mixer.music.play(-1)

    def stop_sound(self) -> None:
        """Stops all currently playing sounds."""
        pygame.mixer.music.stop()
        for sound in self.sounds.values():
            sound.stop()

    def _load_sound(self,filename: str) -> pygame.mixer.Sound:

        """Loads and caches a sound effect if not already loaded."""

        full_path = rf"{self.root}/{filename}"  # Ensure correct path
        if full_path not in self.sounds:
            sound = pygame.mixer.Sound(full_path)
            sound.set_volume(self.sfx_volume)
            self.sounds[full_path] = sound
        return self.sounds[full_path]

    def play_sound(self, filename: str) -> None:

        """Plays a sound effect, loading it first if necessary."""

        sound = self._load_sound(f"{filename}.mp3")
        sound.play()

    def set_background_volume(self, volume: float) -> None:

        """Sets the volume for background music."""

        self.bg_volume = volume
        pygame.mixer.music.set_volume(self.bg_volume)

    def set_sfx_volume(self, volume: float) -> None:

        """Sets the volume for sound effects."""

        self.sfx_volume = volume
        for sound in self.sounds.values():
            sound.set_volume(self.sfx_volume)

    def set_all_volume(self, volume: float) -> None:

        """Sets the overall volume (both background music and sound effects)."""

        self.bg_volume = self.sfx_volume = volume
        pygame.mixer.music.set_volume(self.bg_volume)
        for sound in self.sounds.values():
            sound.set_volume(self.sfx_volume)

    def quit_mixer(self) -> None:

        """Stops all sounds and quits the pygame mixer."""

        self.stop_sound()
        pygame.mixer.quit()
