# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


class TestDivision:
    def test_positive(self, class_timer, test_timer):
        assert all_division(100, 2) == 50

    def test_multiple_divisors(self, test_timer):
        assert all_division(100, 2, 5) == 10

    def test_float(self):
        assert all_division(10, 4) == 2.5

    def test_negative(self):
        assert all_division(-100, 2) == -50

    def test_zero(self):
        with pytest.raises(ZeroDivisionError):
            all_division(10, 0)
