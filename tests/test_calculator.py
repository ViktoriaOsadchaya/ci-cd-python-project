import pytest
import sys
import os
from src.calculator import Calculator

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator import Calculator

class TestCalculator:
    def setup_method(self):
        self.calc = Calculator()

    def test_add(self):
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0

    def test_subtract(self):
        assert self.calc.subtract(5, 3) == 2

    def test_multiply(self):
        assert self.calc.multiply(3, 4) == 12

    def test_divide(self):
        assert self.calc.divide(6, 3) == 2

    def test_divide_by_zero(self):
        with pytest.raises(ValueError):
            self.calc.divide(5, 0)

    def test_power(self):
        assert self.calc.power(2, 3) == 8