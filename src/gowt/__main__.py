""" CLI for gowt """

from __future__ import annotations

import os
from typing import TYPE_CHECKING

from pkgcore.repository import errors as repo_errors
from pkgcore.util.commandline import ArgumentParser, Tool

from . import __version__

if TYPE_CHECKING:
    from pkgcore.ebuild.domain import domain
    from snakeoil.cli.arghparse import Namespace

argparser: ArgumentParser = ArgumentParser(prog="gowt", description="TODO: Add something later")
# argparser.add_argument("-h", "--help", action="help", help="show this help message and exit")
argparser.add_argument("-V", "--version", action="version", version=f"{argparser.prog}: {__version__}", help="print version and exit")
# argparser.add_argument("-f", "--config-file", action="store",
# help=f"{argparser.prog} config file location", dest="config_file", metavar="FILE")
argparser.add_argument("-r", "--repo", action="append", help="provide repository location (default: current directory)")


@argparser.bind_final_check
def _get_repos(parser: ArgumentParser, namespace: Namespace) -> None:
    if namespace.repo is None:
        namespace.repo = [os.getcwd()]
    for repo in namespace.repo:
        try:
            _domain: domain = namespace.domain
            _domain.find_repo(path=repo, config=namespace.config)
        except (repo_errors.InitializationError, OSError) as e:
            parser.error(e)


@argparser.bind_main_func
def _main(options: Namespace, out, err) -> int:  # type: ignore
    print([k for k in options.domain.repos.keys()])  # noqa
    return 0


def main(argparser: ArgumentParser = argparser) -> int:
    tool: Tool = Tool(argparser)
    tool()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
