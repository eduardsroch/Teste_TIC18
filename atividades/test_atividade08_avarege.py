import pytest
from python.atividades.atividade08_average import calculate_average

def test_calculate_average():
    numbers = [1, 2, 3, 4, 5]
    assert calculate_average(numbers) == 3.0

    with pytest.raises(ValueError):
        calculate_average([])

    numbers = [10]
    assert calculate_average(numbers) == 10.0

    numbers = [-1, -2, -3, -4, -5]
    assert calculate_average(numbers) == -3.0

    numbers = [1.5, 2.5, 3.5, 4.5, 5.5]
    assert calculate_average(numbers) == 3.5

    numbers = [1000000, 2000000, 3000000, 4000000, 5000000]
    assert calculate_average(numbers) == 3000000.0

    numbers = [0, 0, 0, 0, 0]
    assert calculate_average(numbers) == 0.0

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert calculate_average(numbers) == 5.5