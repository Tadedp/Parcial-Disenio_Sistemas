"""
Module for the abstract base controller class.
"""

from abc import ABC, abstractmethod
from typing import Type

from schemas.base_schema import BaseSchema
from services.base_service import BaseService


class BaseController(ABC):
    """
    Abstract base controller class.
    """

    @property
    @abstractmethod
    def service(self) -> BaseService:
        """
        Service to access database
        """

    @property
    @abstractmethod
    def schema(self) -> Type[BaseSchema]:
        """
        Pydantic Schema to validate data
        """
