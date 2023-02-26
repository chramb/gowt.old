__all__ = ("domain",)

from typing import Any, AnyStr

from pkgcore.repository import configured

from .repository import UnconfiguredTree
from ..config.domain import domain as config_domain
from ..repository.prototype import tree

class domain(config_domain):
    def __init__(
        self,
        profile: Any,
        repos: Any,
        vdb: Any,
        root: str = "/",
        prefix: str = "/",
        config_dir: str = "/etc/portage",
        **settings: Any,
    ): ...
    def find_repo(self, path: AnyStr, config: Any, configure: bool = False) -> tree: ...  # L:780
    ...
