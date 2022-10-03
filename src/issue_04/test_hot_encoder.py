import pytest

from one_hot_encoder import fit_transform


def test_empty_args():
    with pytest.raises(TypeError) as exc:
        fit_transform()
    exc_message = exc.value.args
    equal = ('expected at least 1 arguments, got 0',)
    assert exc_message == equal, 'Wrong exception message'


def test_one_city_repeat():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    res = fit_transform(cities)
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert res == exp_transformed_cities


def test_several_cities_repeat():
    cities = ['Moscow', 'London', 'Novgorod',
              'Moscow', 'Stavropol', 'Novgorod']
    res = fit_transform(cities)
    exp_transformed_cities = [
        ('Moscow', [0, 0, 0, 1]),
        ('London', [0, 0, 1, 0]),
        ('Novgorod', [0, 1, 0, 0]),
        ('Moscow', [0, 0, 0, 1]),
        ('Stavropol', [1, 0, 0, 0]),
        ('Novgorod', [0, 1, 0, 0]),
    ]
    assert res == exp_transformed_cities


def test_cities_repeat_several_times():
    cities = ['Moscow', 'London', 'Novgorod',
              'Moscow', 'Stavropol', 'Novgorod',
              'Stavropol', 'London', 'Moscow',
              ]
    res = fit_transform(cities)
    exp_transformed_cities = [
        ('Moscow', [0, 0, 0, 1]),
        ('London', [0, 0, 1, 0]),
        ('Novgorod', [0, 1, 0, 0]),
        ('Moscow', [0, 0, 0, 1]),
        ('Stavropol', [1, 0, 0, 0]),
        ('Novgorod', [0, 1, 0, 0]),
        ('Stavropol', [1, 0, 0, 0]),
        ('London', [0, 0, 1, 0]),
        ('Moscow', [0, 0, 0, 1]),
    ]
    assert res == exp_transformed_cities
