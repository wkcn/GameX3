class Sound:
    def __init__(self, filename):
        self.filename = filename

    def play(self, loops=0, fade_ms=0):
        raise NotImplementedError('Sound.play is not implemented')

    def stop(self):
        raise NotImplementedError('Sound.stop is not implemented')
