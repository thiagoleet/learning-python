from flask import request as FlaskRequest
from typing import Dict, List
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from .interfaces.calculator_list_interface import CalculatorListInterface as Calculator


class Calculator2(Calculator):
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self._validate_body(body=body)
        calculate_number = self.__process_data(input_data=input_data)
        formated_response = self._format_response(
            result=calculate_number)
        return formated_response

    def _validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Body mal formatado")

        input_data = body["numbers"]
        return input_data

    def __process_data(self, input_data: List[float]) -> float:
        first_process_result = [(num*11) ** 0.95 for num in input_data]
        result = self.__driver_handler.standard_derivation(
            numbers=first_process_result)
        return 1/result

    def _format_response(self, result: float) -> Dict:
        return {
            "data": {
                "Calculator": 2,
                "result": round(result, 2)
            }}
