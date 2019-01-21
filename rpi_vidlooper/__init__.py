from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

from .vidlooper import VidLooper

__all__ = ['VidLooper']
