from typing import Dict, List
from pytest import raises
from .calculator_3 import Calculator3


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandlerError():
    def variance(self, numbers: List[float]) -> float:
        return 3


class MockDriverHandlerSuccess():
    def variance(self, numbers: List[float]) -> float:
        return 10000000


def test_calculate_with_variance_error():
    mock_request = MockRequest(body={"numbers": [1, 2, 3, 4, 5]})
    calc = Calculator3(driver_handler=MockDriverHandlerError())

    with raises(Exception) as excinfo:
        response = calc.calculate(request=mock_request)

    assert str(
        excinfo.value) == "Falha no processo: Variância menor do que multiplicação"


def test_calculate():
    mock_request = MockRequest(body={"numbers": [1, 1, 1, 1, 100]})
    calc = Calculator3(driver_handler=MockDriverHandlerSuccess())

    response = calc.calculate(request=mock_request)

    assert response == {
        'data': {'Calculator': 3, 'value': 10000000, 'success': True}
    }
