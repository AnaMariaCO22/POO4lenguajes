from _typeshed import Incomplete
from typing import Any

from setuptools import dist

class SetupRequirementsError(BaseException):
    specifiers: Any
    def __init__(self, specifiers) -> None: ...

class Distribution(dist.Distribution):
    def fetch_build_eggs(self, specifiers) -> None: ...
    @classmethod
    def patch(cls) -> None: ...

class _BuildMetaBackend:
    def run_setup(self, setup_script: str = ...) -> None: ...
    def get_requires_for_build_wheel(self, config_settings: Incomplete | None = ...): ...
    def get_requires_for_build_sdist(self, config_settings: Incomplete | None = ...): ...
    def prepare_metadata_for_build_wheel(self, metadata_directory, config_settings: Incomplete | None = ...): ...
    def build_wheel(
        self, wheel_directory, config_settings: Incomplete | None = ..., metadata_directory: Incomplete | None = ...
    ): ...
    def build_sdist(self, sdist_directory, config_settings: Incomplete | None = ...): ...

class _BuildMetaLegacyBackend(_BuildMetaBackend):
    def run_setup(self, setup_script: str = ...) -> None: ...

get_requires_for_build_wheel: Any
get_requires_for_build_sdist: Any
prepare_metadata_for_build_wheel: Any
build_wheel: Any
build_sdist: Any
__legacy__: Any
