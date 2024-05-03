from abc import ABC, abstractmethod
from flask import request as FlaskRequest
from typing import Dict


class CalculatorSingleInterface(ABC):

    @abstractmethod
    def calculate(self, request: FlaskRequest) -> Dict: pass

    @abstractmethod
    def _validate_body(self, body: Dict) -> float: pass

    @abstractmethod
    def _format_response(self, result: float) -> Dict: pass
