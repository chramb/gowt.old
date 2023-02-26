from typing import Any

class tree:
    # raw_repo = None
    # is_supported = True
    # livefs = False
    # package_class = None
    # configured = True
    # frozen_settable = True
    # operations_kls = repo.operations
    # pkg_masks = frozenset()
    def __init__(self, frozen: bool = False): ...
    def configure(self, *args: tuple[Any, ...]) -> None: ...
    @property
    def aliases(self) -> tuple[Any | None, ...]: ...
