from __future__ import annotations

from typing import TYPE_CHECKING

from pkgcore.config import load_config

if TYPE_CHECKING:
    from pathlib import Path

    from pkgcore.config.central import CompatConfigManager
    from pkgcore.ebuild.domain import domain
    from pkgcore.ebuild.repository import UnconfiguredTree


def get_repo(path: Path, config: Path | None = None) -> (domain, UnconfiguredTree):
    ...
    c: CompatConfigManager = load_config(path=config if config is not None else None)
    d: domain = c.get_default("domain")
    for repo in reversed(sorted(d.ebuild_repos_raw, key=lambda x: len(x.location))):  # type: ignore # noqa
        p = path
        while not p.samefile(p / ".."):
            if p.samefile(repo.location):
                return (d, repo)
            p = p / ".."

    # fallback to unconfigured repo search
    return (d, d.find_repo(str(path), config=c, configure=False))
