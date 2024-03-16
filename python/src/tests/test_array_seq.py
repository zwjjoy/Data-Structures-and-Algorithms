import pytest

from src.sequence.Array_seq import Array_seq

def test_array_seq():
    a = Array_seq()
    for i in range(10):
        a.insert_last(i)

    for i in range(10):
        assert a.get_at(i) == i

    with pytest.raises(IndexError):
        a.get_at(10)

    with pytest.raises(IndexError):
        a.set_at(10, 10)
        
    a.set_at(0, 10)
    assert a.get_at(0) == 10

    a.delete_last()
    assert len(a) == 9

    a.delete_first()
    assert len(a) == 8

    a.insert_first(10)
    assert len(a) == 9

    a.insert_last(10)
    assert len(a) == 10

    a.delete_at(0)
    assert len(a) == 9

    a.build([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    assert len(a) == 10
    assert list(a) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]