from dataclasses import dataclass
from enum import Enum
from typing import Any, TypeVar


@dataclass
class Pagination:
    """Limit offset pagination parameters"""

    page: int = 1
    limit: int = 10


class SortingDirection(Enum):
    ascending = 0
    descending = 1


type ModelData = dict[str, Any]
type ByFilter = dict[str, Any]
type InFilter = dict[str, list[Any]]
type InRangeFilter = dict[str, tuple[Any, Any]]
type SearchFilter = dict[str, str]
type NotNullFilter = list[str]
type Sorting = dict[str, SortingDirection]
