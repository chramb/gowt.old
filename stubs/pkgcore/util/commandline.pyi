from typing import Any

from snakeoil.cli import arghparse, tool

class ArgumentParser(arghparse.ArgumentParser):
    def __init__(
        self,
        suppress: bool = False,
        help: bool = True,
        config: bool = True,
        domain: bool = True,
        global_config: Any = (),
        **kwds: Any,
    ): ...

class Tool(tool.Tool):
    def pre_parse(self, *args: Any, **kwargs: Any) -> None: ...
