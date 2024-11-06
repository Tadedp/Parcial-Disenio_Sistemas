"""Base controller implementation module."""
from typing import Type
from fastapi import APIRouter

from controllers.base_controller import BaseController
from schemas.base_schema import BaseSchema
from services.base_service import BaseService


class BaseControllerImpl(BaseController):
    """Base controller implementation."""
    def __init__(self, schema: Type[BaseSchema], service: BaseService,):
        self.service = service
        self.schema = schema
        # APIRouter instance to handle routing related to a particular resource for the controller
        self.router = APIRouter()  

    @property
    def service(self) -> BaseService:
        """Service to access database."""
        return self._service

    @property
    def schema(self) -> Type[BaseSchema]:
        """Pydantic Schema to validate data."""
        return self._schema

    @schema.setter
    def schema(self, value):
        self._schema = value

    @service.setter
    def service(self, value):
        self._service = value
