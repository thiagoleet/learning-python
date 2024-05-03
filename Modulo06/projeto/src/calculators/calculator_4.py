from flask import request as FlaskRequest
from typing import Dict, List
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from .interfaces.calculator_single_interface import CalculatorSingleInterface as Calculator


class Calculator4(Calculator):

    def __init__(self):
        pass

    def calculate(self, request: FlaskRequest):
        body = request.json
        numbers = self._validate_body(body=body)
        calculated_average = self.__calculate_average(numbers=numbers)
        formated_response = self._format_response(
            result=calculated_average)
        return formated_response

    def _validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Body mal formatado")
        numbers = body["numbers"]

        if type(numbers) is not list:
            raise HttpUnprocessableEntityError("Formato inválido")
        return numbers

    def __calculate_average(self, numbers: List[float]) -> float:
        average = sum(numbers) / len(numbers)
        return average

    def _format_response(self, result: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "result": round(result, 2)
            }
        }
