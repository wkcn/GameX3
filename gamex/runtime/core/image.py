import functools
from ..platform.graph import Surface


@functools.lru_cache()
def load(filename):
    return Surface.load(filename)
