import main
import unittest


class TestMain(unittest.TestCase):

    def test_convert(self):
        self._assert_roman(1, 'I')
        self._assert_roman(2, 'II')
        self._assert_roman(3, 'III')
        self._assert_roman(4, 'IV')
        self._assert_roman(5, 'V')
        self._assert_roman(6, 'VI')
        self._assert_roman(7, 'VII')
        self._assert_roman(9, 'IX')
        self._assert_roman(10, 'X')
        self._assert_roman(20, 'XX')
        self._assert_roman(40, 'XL')

    def _assert_roman(self, arabic, roman):
        result = main.to_romans(arabic)

        self.assertEqual(result, roman, 'arabic: {0}, expected: {1}, got: {2} '.format(arabic, roman, result))

if __name__ == '__main__':
    unittest.main()
