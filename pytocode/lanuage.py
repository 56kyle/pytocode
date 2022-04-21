
from typing import Generic, TypeVar


T = TypeVar('T')
K = TypeVar('K')
V = TypeVar('V')


class Language:
    def __init__(self, *args, **kwargs):
        pass

    def func(self):
        raise NotImplementedError

    def cls(self):
        raise NotImplementedError

