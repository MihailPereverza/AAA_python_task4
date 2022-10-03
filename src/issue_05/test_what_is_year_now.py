from unittest.mock import MagicMock, patch

import pytest

from what_is_year_now import what_is_year_now


def create_mock_cm(data: bytes):
    cm = MagicMock()
    cm.read.return_value = data
    cm.__enter__.return_value = cm
    return cm


@patch('urllib.request.urlopen')
def test_dmy_format(mock_urlopen: MagicMock):
    mock_urlopen.return_value = create_mock_cm(
        b'{"currentDateTime":"01.03.2019T14:56Z"}'
    )
    res = what_is_year_now()

    assert res == 2019
    mock_urlopen.assert_called_once_with(
        'http://worldclockapi.com/api/json/utc/now'
    )


@patch('urllib.request.urlopen')
def test_ymd_format(mock_urlopen: MagicMock):
    mock_urlopen.return_value = create_mock_cm(
        b'{"currentDateTime":"2019-10-03T14:56Z"}'
    )
    res = what_is_year_now()

    assert res == 2019
    mock_urlopen.assert_called_once_with(
        'http://worldclockapi.com/api/json/utc/now'
    )


@patch('urllib.request.urlopen')
def test_invalid_date(mock_urlopen: MagicMock):
    mock_urlopen.return_value = create_mock_cm(
        b'{"currentDateTime":"who is it?T14:56Z"}'
    )
    with pytest.raises(ValueError) as exc:
        what_is_year_now()

    assert exc.value.args == ('Invalid format', )
    mock_urlopen.assert_called_once_with(
        'http://worldclockapi.com/api/json/utc/now'
    )
