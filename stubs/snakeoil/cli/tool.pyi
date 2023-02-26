from argparse import ArgumentParser
from typing import IO, Optional, Any, Callable

class Tool:
    # Check arghparse or argparse
    def __init__(
        self,
        parser: ArgumentParser,
        outfile: Optional[IO[Any]] = None,
        errfile: Optional[IO[Any]] = None,
    ): ...
    def __call__(self, args: Optional[Any] = ...) -> int | None: ...  # self.main() -> e.code: int L:71
