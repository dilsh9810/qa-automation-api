import pytest

def g():
    raise SystemError(1)

def test_myfirstError():
    with pytest.raises(SystemError):
        g()

