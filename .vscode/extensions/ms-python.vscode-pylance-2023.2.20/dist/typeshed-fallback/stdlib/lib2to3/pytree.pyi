from _typeshed import Self
from collections.abc import Iterator
from lib2to3.pgen2.grammar import Grammar
from typing import Any
from typing_extensions import TypeAlias

_NL: TypeAlias = Node | Leaf
_Context: TypeAlias = tuple[str, int, int]
_Results: TypeAlias = dict[str, _NL]
_RawNode: TypeAlias = tuple[int, str, _Context, list[_NL] | None]

HUGE: int

def type_repr(type_num: int) -> str: ...

class Base:
    type: int
    parent: Node | None
    prefix: str
    children: list[_NL]
    was_changed: bool
    was_checked: bool
    def __eq__(self, other: object) -> bool: ...
    def _eq(self: Self, other: Self) -> bool: ...
    def clone(self: Self) -> Self: ...
    def post_order(self) -> Iterator[_NL]: ...
    def pre_order(self) -> Iterator[_NL]: ...
    def replace(self, new: _NL | list[_NL]) -> None: ...
    def get_lineno(self) -> int: ...
    def changed(self) -> None: ...
    def remove(self) -> int | None: ...
    @property
    def next_sibling(self) -> _NL | None: ...
    @property
    def prev_sibling(self) -> _NL | None: ...
    def leaves(self) -> Iterator[Leaf]: ...
    def depth(self) -> int: ...
    def get_suffix(self) -> str: ...

class Node(Base):
    fixers_applied: list[Any]
    def __init__(
        self,
        type: int,
        children: list[_NL],
        context: Any | None = None,
        prefix: str | None = None,
        fixers_applied: list[Any] | None = None,
    ) -> None: ...
    def set_child(self, i: int, child: _NL) -> None: ...
    def insert_child(self, i: int, child: _NL) -> None: ...
    def append_child(self, child: _NL) -> None: ...
    def __unicode__(self) -> str: ...

class Leaf(Base):
    lineno: int
    column: int
    value: str
    fixers_applied: list[Any]
    def __init__(
        self, type: int, value: str, context: _Context | None = None, prefix: str | None = None, fixers_applied: list[Any] = ...
    ) -> None: ...
    def __unicode__(self) -> str: ...

def convert(gr: Grammar, raw_node: _RawNode) -> _NL: ...

class BasePattern:
    type: int
    content: str | None
    name: str | None
    def optimize(self) -> BasePattern: ...  # sic, subclasses are free to optimize themselves into different patterns
    def match(self, node: _NL, results: _Results | None = None) -> bool: ...
    def match_seq(self, nodes: list[_NL], results: _Results | None = None) -> bool: ...
    def generate_matches(self, nodes: list[_NL]) -> Iterator[tuple[int, _Results]]: ...

class LeafPattern(BasePattern):
    def __init__(self, type: int | None = None, content: str | None = None, name: str | None = None) -> None: ...

class NodePattern(BasePattern):
    wildcards: bool
    def __init__(self, type: int | None = None, content: str | None = None, name: str | None = None) -> None: ...

class WildcardPattern(BasePattern):
    min: int
    max: int
    def __init__(self, content: str | None = None, min: int = 0, max: int = 2147483647, name: str | None = None) -> None: ...

class NegatedPattern(BasePattern):
    def __init__(self, content: str | None = None) -> None: ...

def generate_matches(patterns: list[BasePattern], nodes: list[_NL]) -> Iterator[tuple[int, _Results]]: ...