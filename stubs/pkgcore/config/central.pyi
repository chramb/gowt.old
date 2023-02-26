from typing import Optional, Any, Tuple, Union

from . import basics

class CollapsedConfig:
    def __init__(
        self,
        type_obj: basics.ConfigType,
        config: dict[str, Any],
        manager: Optional[Any],
        debug: bool = False,
        default: bool = False,
    ): ...

class ConfigManager:
    def __init__(self, configs: dict[str, basics.ConfigSection] | tuple[()] = (), debug: bool = False): ...
