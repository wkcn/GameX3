from ..platform.audio import Sound as SoundBase


class _EmptyChannel:
    pass


CHANNELS = dict()


class Sound:
    def __init__(self, sound, channel):
        self.sound = SoundBase(sound)
        self.channel = channel

    def play(self, loops=0, fade_ms=0):
        if self.channel != _EmptyChannel:
            old_sound = CHANNELS.get(self.channel)
            if old_sound:
                old_sound.stop()
        self.sound.play(loops=loops, fade_ms=fade_ms)
        CHANNELS[self.channel] = self.sound

    def stop(self):
        self.sound.stop()
        if CHANNELS.get(self.channel) == self.sound:
            del CHANNELS[self.channel]


def load(filename):
    return Sound(filename, channel=_EmptyChannel)


def load_bgm(filename, channel=None):
    return Sound(filename, channel=channel)
