import pytest
from python.atividades.atividade13_factorial import factorial

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800 

    with pytest.raises(ValueError):
        factorial(-1)

    with pytest.raises(ValueError):
        factorial(-10)
