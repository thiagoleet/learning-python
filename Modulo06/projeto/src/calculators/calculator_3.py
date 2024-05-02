from flask import request as FlaskRequest
from typing import Dict, List
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface


class Calculator3:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body=body)

        variance = self.__calculate_variance(numbers=input_data)
        multiplication = self.__calculate_multiplication(numbers=input_data)
        self.__verify_results(variance=variance, multiplication=multiplication)
        formated_response = self.__format_response(variance=variance)

        return formated_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise Exception("Body mal formatado")

        input_data = body["numbers"]
        return input_data

    def __calculate_variance(self, numbers: List[float]) -> float:
        variance = self.__driver_handler.variance(numbers=numbers)
        return variance

    def __calculate_multiplication(self, numbers: List[float]) -> float:
        multiplication = 1
        for num in numbers:
            multiplication *= num

        return multiplication

    def __verify_results(self, variance: float, multiplication: float) -> None:
        if variance < multiplication:
            raise Exception(
                "Falha no processo: Variância menor do que multiplicação")

    def __format_response(self, variance: float) -> Dict:
        return {"data": {
            "Calculator": 3,
            "value": variance,
            "success": True
        }}
