from typing import Dict, List
from pytest import raises
from .calculator_2 import Calculator2


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandler():
    def standard_derivation(self, numbers: List[float]) -> float:
        return 3


# Integração entre Numpy Handler e Calculator2


def test_calculate_integration():
    mock_request = MockRequest(body={"numbers": [2.12, 4.62, 1.32]})
    driver = MockDriverHandler()
    calc = Calculator2(driver_handler=driver)

    response = calc.calculate(request=mock_request)

    assert isinstance(response, dict)
    assert response == {
        'data':
        {
            'Calculator': 2,
            'result': 0.33
        }
    }


def test_calculate():
    mock_request = MockRequest(body={"numbers": [2.12, 4.62, 1.32]})
    driver = MockDriverHandler()
    calc = Calculator2(driver_handler=driver)

    response = calc.calculate(request=mock_request)

    # Formato da resposta
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]

    # Assertividade da resposta
    assert response["data"]["result"] == 0.33
    assert response["data"]["Calculator"] == 2


def test_calculate_with_body_error():
    mock_request = MockRequest(body={"something": 1})
    driver = MockDriverHandler()

    calc = Calculator2(driver_handler=driver)

    with raises(Exception) as excinfo:
        calc.calculate(request=mock_request)

    assert str(excinfo.value) == "Body mal formatado"
