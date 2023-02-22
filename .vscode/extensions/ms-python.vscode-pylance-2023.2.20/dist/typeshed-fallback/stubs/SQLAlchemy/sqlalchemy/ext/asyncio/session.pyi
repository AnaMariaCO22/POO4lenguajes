from _typeshed import Incomplete, Self
from typing import Any

from ...util import memoized_property
from .base import ReversibleProxy, StartableContext

class AsyncSession(ReversibleProxy):
    dispatch: Any
    bind: Any
    binds: Any
    sync_session_class: Any
    sync_session: Any
    def __init__(
        self, bind: Incomplete | None = ..., binds: Incomplete | None = ..., sync_session_class: Incomplete | None = ..., **kw
    ) -> None: ...
    async def refresh(self, instance, attribute_names: Incomplete | None = ..., with_for_update: Incomplete | None = ...): ...
    async def run_sync(self, fn, *arg, **kw): ...
    async def execute(
        self, statement, params: Incomplete | None = ..., execution_options=..., bind_arguments: Incomplete | None = ..., **kw
    ): ...
    async def scalar(
        self, statement, params: Incomplete | None = ..., execution_options=..., bind_arguments: Incomplete | None = ..., **kw
    ): ...
    async def scalars(
        self, statement, params: Incomplete | None = ..., execution_options=..., bind_arguments: Incomplete | None = ..., **kw
    ): ...
    async def get(
        self,
        entity,
        ident,
        options: Incomplete | None = ...,
        populate_existing: bool = ...,
        with_for_update: Incomplete | None = ...,
        identity_token: Incomplete | None = ...,
    ): ...
    async def stream(
        self, statement, params: Incomplete | None = ..., execution_options=..., bind_arguments: Incomplete | None = ..., **kw
    ): ...
    async def stream_scalars(
        self, statement, params: Incomplete | None = ..., execution_options=..., bind_arguments: Incomplete | None = ..., **kw
    ): ...
    async def delete(self, instance): ...
    async def merge(self, instance, load: bool = ..., options: Incomplete | None = ...): ...
    async def flush(self, objects: Incomplete | None = ...) -> None: ...
    def get_transaction(self): ...
    def get_nested_transaction(self): ...
    def get_bind(self, mapper: Incomplete | None = ..., clause: Incomplete | None = ..., bind: Incomplete | None = ..., **kw): ...
    async def connection(self, **kw): ...
    def begin(self, **kw): ...
    def begin_nested(self, **kw): ...
    async def rollback(self): ...
    async def commit(self): ...
    async def close(self): ...
    @classmethod
    async def close_all(cls): ...
    async def __aenter__(self: Self) -> Self: ...
    async def __aexit__(self, type_, value, traceback) -> None: ...
    # proxied from Session
    identity_map: Any
    autoflush: Any
    @classmethod
    def identity_key(cls, *args, **kwargs): ...
    @classmethod
    def object_session(cls, instance): ...
    def __contains__(self, instance): ...
    def __iter__(self): ...
    def add(self, instance, _warn: bool = ...) -> None: ...
    def add_all(self, instances) -> None: ...
    def expire(self, instance, attribute_names: Incomplete | None = ...) -> None: ...
    def expire_all(self) -> None: ...
    def expunge(self, instance) -> None: ...
    def expunge_all(self) -> None: ...
    def is_modified(self, instance, include_collections: bool = ...): ...
    def in_transaction(self): ...
    def in_nested_transaction(self): ...
    @property
    def no_autoflush(self) -> None: ...
    @property
    def is_active(self): ...
    @property
    def dirty(self): ...
    @property
    def deleted(self): ...
    @property
    def new(self): ...
    @memoized_property
    def info(self): ...

class _AsyncSessionContextManager:
    async_session: Any
    def __init__(self, async_session) -> None: ...
    trans: Any
    async def __aenter__(self): ...
    async def __aexit__(self, type_, value, traceback) -> None: ...

class AsyncSessionTransaction(ReversibleProxy, StartableContext):
    session: Any
    nested: Any
    sync_transaction: Any
    def __init__(self, session, nested: bool = ...) -> None: ...
    @property
    def is_active(self): ...
    async def rollback(self) -> None: ...
    async def commit(self) -> None: ...
    async def start(self, is_ctxmanager: bool = ...): ...
    async def __aexit__(self, type_, value, traceback) -> None: ...

def async_object_session(instance): ...
def async_session(session): ...
