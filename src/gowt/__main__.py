""" CLI for gowt """

from __future__ import annotations

# Standard Library imports
import os
import textwrap

# Third-party imports
from pkgcore.repository import errors as repo_errors
from pkgcore.util.commandline import ArgumentParser, Tool

# Local imports
from gowt import __version__

if __debug__:
    # Type imports
    from pkgcore.ebuild.domain import domain  # isort:skip
    from pkgcore.config.central import ConfigManager  # isort:skip
    from pkgcore.repository.filtered import tree as filtered_tree  # isort:skip
    from pkgcore.ebuild.repository import UnconfiguredTree  # isort:skip
    from snakeoil.cli.arghparse import Namespace  # isort:skip


argparser = ArgumentParser()
argparser.add_argument("--version", "-V", action="version", version=f"gowt: {__version__}", help="print version and exit")  # noqa: E501
argparser.add_argument("--repo", "-r", "-C", action="store", help="repository location")
argparser.add_argument("--gentoo", action="store", help="::gentoo repository location")


@argparser.bind_final_check
def _get_repo(parser: ArgumentParser, namespace: Namespace) -> None:
    if namespace.gentoo:
        namespace.domain.add_repo(path=namespace.gentoo, config=namespace.config)
    elif "gentoo" not in namespace.domain.repos:
        msg: str = textwrap.dedent(
            """
            Gentoo master repo not found (didn't check if needed)
            please sync it or provide it's location with --gentoo flag
            """
        ).strip()
        raise parser.error(msg)

    repo: UnconfiguredTree
    try:
        if namespace.repo is None:
            _domain: domain = namespace.domain
            _config: ConfigManager = namespace.config
            repo = _domain.find_repo(path=os.getcwd(), config=_config)
        else:
            repo = namespace.domain.find_repo(path=namespace.repo, config=namespace.config)
    except (repo_errors.InitializationError, OSError) as e:
        raise parser.error(e)

    if repo is None:
        raise parser.error(f"Not in ebuild repo, please specify repo location with --repo/-C or run {__name__} from repo")

    namespace.repo = repo


@argparser.bind_main_func
def _main(options: Namespace, out, err) -> None:  # type: ignore
    _repo: filtered_tree = options.repo
    print(__debug__)
    print(_repo.aliases)


def main() -> None:
    tool = Tool(argparser)
    raise SystemExit(tool())


if __name__ == "__main__":
    main()
