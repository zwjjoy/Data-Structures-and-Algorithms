import pytest

from src.sequence.StaticArray import StaticArray

def test_static_array():
    a = StaticArray(10)
    for i in range(10):
        a.set_at(i, i)

    for i in range(10):
        assert a.get_at(i) == i

    with pytest.raises(IndexError):
        a.get_at(10)

    with pytest.raises(IndexError):
        a.set_at(10, 10)
        
    a.set_at(0, 10)
    assert a.get_at(0) == 10