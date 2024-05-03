from src.calculators.calculator_1 import Calculator1
from src.calculators.calculator_2 import Calculator2
from src.calculators.calculator_3 import Calculator3
from src.calculators.calculator_4 import Calculator4

from src.drivers.numpy_handler import NumpyHandler


def calculator1_factory() -> Calculator1:
    calc = Calculator1()
    return calc


def calculator2_factory() -> Calculator2:
    numpy_handler = NumpyHandler()
    calc = Calculator2(driver_handler=numpy_handler)
    return calc


def calculator3_factory() -> Calculator3:
    numpy_handler = NumpyHandler()
    calc = Calculator3(driver_handler=numpy_handler)
    return calc


def calculator4_factory() -> Calculator4:
    calc = Calculator4()
    return calc
