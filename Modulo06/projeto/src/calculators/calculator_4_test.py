from typing import Dict, List
from pytest import raises
from .calculator_4 import Calculator4


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def test_calculate():
    mock_request = MockRequest(body={"numbers": [1, 2, 3, 4, 5]})
    calc = Calculator4()

    response = calc.calculate(request=mock_request)

    assert isinstance(response, dict)
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]

    assert response["data"]["Calculator"] == 4
    assert response["data"]["result"] == 3


def test_calculate_with_body_error():
    mock_request = MockRequest(body={"something": [1, 2, 3, 4, 5]})
    calc = Calculator4()

    with raises(Exception) as excinfo:
        calc.calculate(request=mock_request)

    assert str(excinfo.value) == "Body mal formatado"


def test_calculate_with_wrong_format():
    mock_request = MockRequest(body={"numbers": 420})
    calc = Calculator4()

    with raises(Exception) as excinfo:
        calc.calculate(request=mock_request)

    assert str(excinfo.value) == "Formato inválido"
