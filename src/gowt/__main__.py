""" GOWT cli """

from __future__ import annotations

from argparse import ArgumentParser
import itertools
from os import getcwd
from pathlib import Path

from pkgcore.ebuild.domain import domain as Domain
from pkgcore.ebuild.repository import UnconfiguredTree

from .repository import get_repo

argparser = ArgumentParser()
argparser.add_argument("--repo", "-r", help="repository location", action="append")
parsed = argparser.parse_args()


def main() -> int:
    repos = []
    for repo in parsed.repo:
        repo_path = Path(getcwd() + "/" + repo)
        tree: UnconfiguredTree
        domain: Domain
        domain, tree = get_repo(repo_path)
        if tree is not None:
            # typing: off
            repository = itertools.groupby(tree, lambda pkg: pkg.category)
            for (
                key,
                cat,
            ) in repository:
                for p in cat:
                    print(p.key, p.PV, sep="-")
            # typing: on
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
