# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.parametrize('numbers, result', [pytest.param
        ((100, 2), 50, marks=pytest.mark.smoke),
        ((100, 2, 5), 10),
        ((10, 4), 2.5),
        ((-100, 2), -50),
        pytest.param((0, 0), None, marks=pytest.mark.skip('чиним'))])

def test_division(numbers, result):
    assert all_division(*numbers) == result