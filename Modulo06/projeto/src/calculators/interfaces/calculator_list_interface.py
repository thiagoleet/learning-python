from abc import ABC, abstractmethod
from flask import request as FlaskRequest
from typing import Dict, List
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface


class CalculatorListInterface(ABC):
    @abstractmethod
    def __init__(self, driver_handler: DriverHandlerInterface) -> None: pass

    @abstractmethod
    def calculate(self, request: FlaskRequest) -> Dict: pass

    @abstractmethod
    def _validate_body(self, body: Dict) -> List[float]: pass

    @abstractmethod
    def _format_response(self, result: float) -> Dict: pass
