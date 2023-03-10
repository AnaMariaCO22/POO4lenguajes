from _typeshed import Incomplete
from typing import Any

class ProfileStatsFile:
    force_write: Any
    write: Any
    fname: Any
    short_fname: Any
    data: Any
    dump: Any
    sort: Any
    def __init__(self, filename, sort: str = ..., dump: Incomplete | None = ...): ...
    @property
    def platform_key(self): ...
    def has_stats(self): ...
    def result(self, callcount): ...
    def reset_count(self) -> None: ...
    def replace(self, callcount) -> None: ...

def function_call_count(variance: float = ..., times: int = ..., warmup: int = ...): ...
def count_functions(variance: float = ...) -> None: ...
