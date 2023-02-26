__all__ = ("tree",)

from typing import Any
from . import prototype

class tree(prototype.tree):
    # def __init__(self, repo, restrict, sentinel_val=False): ...
    # def itermatch(self, restrict, **kwds) -> Any: ...
    # return self.filterfunc(self.restrict.match, self.raw_repo.itermatch(restrict, ***kwds))
    def __len__(self) -> int: ...
    # __getattr__
    # __dir__
