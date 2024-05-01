import numpy as np
from typing import List

# Facade pattern


class NumpyHandler:
    def __init__(self) -> None:
        self.__np = np

    def standard_derivation(self, numbers: List[float]) -> float:
        return self.__np.std(numbers)
