import unittest

from one_hot_encoder import fit_transform


class TestFitTransform(unittest.TestCase):
    def test_empty_args(self):
        with self.assertRaises(TypeError) as exc:
            fit_transform()
        exc_message = str(exc.exception)
        equal = 'expected at least 1 arguments, got 0'
        self.assertEqual(exc_message, equal, 'Wrong exception message')

    def test_one_city_repeat(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        res = fit_transform(cities)
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(res, exp_transformed_cities)

    def test_several_cities_repeat(self):
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
        self.assertEqual(res, exp_transformed_cities)

    def test_cities_repeat_several_times(self):
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
        self.assertEqual(res, exp_transformed_cities)
