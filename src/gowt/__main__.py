""" GOWT cli """

from __future__ import annotations

from argparse import ArgumentParser
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
        print(domain.all_ebuild_repos_raw)
        print(tree.packages)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
