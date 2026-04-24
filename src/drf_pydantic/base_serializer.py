import json
import warnings

from typing import Any, ClassVar, Dict, Generic, List, Optional, Type, TypeVar

import pydantic

from rest_framework import serializers  # type: ignore
from rest_framework.settings import api_settings  # type: ignore

from drf_pydantic.config import DrfConfigDict

T = TypeVar("T", bound=Dict[str, Any])
P = TypeVar("P", bound=pydantic.BaseModel)


class DrfPydanticSerializer(serializers.Serializer, Generic[P]):
    _pydantic_model: Type[P]
    _drf_config: ClassVar[DrfConfigDict]

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)  # type: ignore
        self.__pydantic_instance: Optional[P] = None

    @property
    def pydantic_instance(self) -> P:
        pass

    def validate(self, attrs: T) -> T:
        pass
