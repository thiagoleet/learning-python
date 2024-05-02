from flask import request as FlaskRequest
from typing import Dict, List
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


class Calculator4:

    def __init__(self):
        pass

    def calculate(self, request: FlaskRequest):
        body = request.json
        numbers = self.__validate_body(body=body)
        calculated_average = self.__calculate_average(numbers=numbers)
        formated_response = self.__format_response(
            average=calculated_average)
        return formated_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Body mal formatado")
        numbers = body["numbers"]

        if type(numbers) is not list:
            raise HttpUnprocessableEntityError("Formato inválido")
        return numbers

    def __calculate_average(self, numbers: List[float]) -> float:
        average = sum(numbers) / len(numbers)
        return average

    def __format_response(self, average: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "result": round(average, 2)
            }
        }
