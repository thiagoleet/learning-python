import numpy as np
from typing import List
from .interfaces.driver_handler_interface import DriverHandlerInterface

# Facade pattern


class NumpyHandler(DriverHandlerInterface):
    def __init__(self) -> None:
        self.__np = np

    def standard_derivation(self, numbers: List[float]) -> float:
        return self.__np.std(numbers)
