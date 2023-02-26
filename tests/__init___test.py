from gowt import __version__

from flit_core.versionno import normalise_version


def test_version() -> None:
    assert __version__ == normalise_version(__version__)
