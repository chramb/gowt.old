import argparse
from argparse import (
    _UNRECOGNIZED_ARGS_ATTR,
    OPTIONAL,
    PARSER,
    REMAINDER,
    SUPPRESS,
    ZERO_OR_MORE,
    ArgumentError,
    # _,
    _get_action_name,
    _SubParsersAction,
    _ArgumentGroup,
)
from typing import Any, Callable, Optional, Iterable, Sequence, NoReturn, Self, TypeVar

from typing_extensions import override

class CsvHelpFormatter(argparse.HelpFormatter):  # L:545
    def _format_args(self, action: argparse.Action, default_metavar: str) -> str: ...  # L:548

class SortedHelpFormatter(CsvHelpFormatter):  # L:565
    def add_argument(self, action: argparse.Action) -> None: ...  # L:568

class Namespace(argparse.Namespace):  # L:573
    def pop(self, key: Any, default: Any = ...) -> object: ...  # L:576
    def __getattr__(self, name: Any) -> Any: ...
    def __bool__(self) -> bool: ...

class OptionalsParser(argparse.ArgumentParser):  # L:666
    # args: anything that can be cast to list(args)
    def parse_known_optionals(self, args: Sequence[str], namespace: Optional[Any] = ...) -> Any | None: ...  # L:669
    def _parse_optionals(self, arg_strings: Sequence[str], namespace: Namespace) -> Any | None: ...

class CsvActionsParser(argparse.ArgumentParser):  # L:974
    # args: tuple[Any]; kwargs: dict[str, Any]
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class ArgumentParser(OptionalsParser, CsvActionsParser):  # L:987
    # kwargs: dict[str, Any]
    def __init__(
        self,
        suppress: Optional[bool] = ...,
        subcmds: Optional[bool] = ...,
        color: Optional[bool] = ...,
        debug: Optional[bool] = ...,
        quiet: Optional[bool] = ...,
        verbose: Optional[bool] = ...,
        version: Optional[bool] = ...,
        add_help: Optional[bool] = ...,
        sorted_help: Optional[bool] = ...,
        description: Optional[str] = ...,
        docs: Optional[str] = ...,
        script: Optional[str] = ...,
        prog: Optional[str] = ...,
        **kwargs: Any,
    ):
        self.debug: bool
        self.verbosity: int
        # ... __stuff()
        self._parents: tuple[Any | None]
        self.description: str
        formatter: SortedHelpFormatter | CsvHelpFormatter

        # super()

        if not suppress:
            base_opts: _ArgumentGroup

        if subcmds:
            prefix: str
            subcmd_modules: Any
            subparsers: Any
    def _update_desc(self, description: Optional[str] = ..., docs: Optional[str] = ...) -> Optional[str]: ...  # L:1160
    # ASK: if description is not None: ??? Breaks `python -OO`
    # @klass.cached_property
    # def parsers(self)->?:
    # @klass.cached_property
    # def subparsers(self)->?:
    def pre_parse(self, namespace: Namespace | None = ...) -> Namespace: ...  # L:1193
    # ASK: Optional vs "| None"
    # mypy errors:
    # def parse_known_args(self, args: Sequence[str] | None = ..., namespace: Namespace | None = ...) -> tuple[Namespace, list[str]]: ... # L:1215
    # def parse_args(self, args: Sequence[str] | None = ...) -> Namespace: ... # L:1260
    def error(self, message: str) -> NoReturn: ...  # L:1320
    def bind_main_func(
        self, functor: Callable[[Namespace, Any, Any], Optional[Any]]
    ) -> Callable[[Namespace, Any, Any], Optional[Any]]: ...  # L:1331
    def bind_class(self, obj: object) -> Self: ...  # L:1339
    def bind_reset_defaults(
        self, functor: Callable[[Namespace, Any, Any], Optional[Any]]
    ) -> Callable[[Namespace, Any, Any], Optional[Any]]: ...  # L:1347
    def bind_delayed_default(
        self, priority: Any | int, name: Optional[str]
    ) -> Callable[[Namespace, Any, Any], Optional[Any]]: ...  # L:1352
    def bind_parse_priority(self, priority: Any) -> Callable[[Namespace, Any, Any], Optional[Any]]: ...  # L:1366
    # def add_subparsers(...) -> _SubParsersAction[_ArgumentParserT]: ... # L:1374
    def bind_pre_parse(
        self, functor: Callable[[Namespace, Any, Any], Optional[Any]]
    ) -> Callable[[Namespace, Any, Any], Any | None]: ...  # L:1388
    def bind_early_parse(
        self, functor: Callable[[Namespace, Any, Any], Optional[Any]]
    ) -> Callable[[Namespace, Any, Any], Any | None]: ...  # L:1393
    def bind_final_check(self, functor: Callable[[Any, Namespace], Optional[Any]]) -> Callable[[Any], Any]: ...  # L: 1398
