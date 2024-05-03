from flask import Blueprint, jsonify, request
from src.main.factories.calculator_factory import calculator1_factory, calculator2_factory, calculator3_factory, calculator4_factory
from src.errors.error_controller import handle_errors
from src.errors.http_bad_request import HttpBadRequestError
from src.calculators.interfaces.calculator_interface import CalculatorBaseInterface as Calculator
calc_route_bp = Blueprint("calc_routes", __name__)


@calc_route_bp.route("/calculator/<int:calc_id>", methods=["POST"])
def calculator_1(calc_id: int):

    calc: Calculator = None

    if calc_id == 1:
        calc = calculator1_factory()
    elif calc_id == 2:
        calc = calculator2_factory()
    elif calc_id == 3:
        calc = calculator3_factory()
    elif calc_id == 4:
        calc = calculator4_factory()

    try:
        if calc is None:
            raise HttpBadRequestError("Calculadora inválida")

        response = calc.calculate(request=request)
        return jsonify(response), 200

    except Exception as error:
        error_response = handle_errors(error=error)
        return jsonify(error_response["body"]), error_response["status_code"]
