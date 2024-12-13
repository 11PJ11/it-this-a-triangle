import unittest
from src.example import is_triangle
from parameterized import parameterized


class TestExample(unittest.TestCase):
    @parameterized.expand([
        (1, 1, 1, True),
        (1, 2, 3, False),
        (2, 4, 6, False),
        (6, 4, 2, False),
        (4, 6, 2, False),
        (-5, 1, 3, False),
    ])
    def test_is_triangle(self, a, b, c, expected):
        self.assertEqual(is_triangle(a, b, c), expected)


if __name__ == '__main__':
    unittest.main()
