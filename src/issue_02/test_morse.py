import pytest

from morse import decode


@pytest.mark.parametrize(('param', 'equal'),
                         [
                             ('.- -- --- --. ..- ...', 'AMOGUS'),
                             ('.-          -...', 'AB'),
                             ('', ''),
                          ])
def test_decode(param: str, equal: str):
    res = decode(param)
    assert res == equal
