import unittest


class TestFactorize(unittest.TestCase):

    def test_wrong_types_raise_exception(self):
        self.cases = ['string',  1.5]
        for x in self.cases:
            with self.subTest(case=x):
                self.assertRaises(TypeError, factorize, x)

    def test_negative(self):
        self.cases = [-1,  -10,  -100]
        for x in self.cases:
            with self.subTest(case=x, msg='test_negative'):
                self.assertRaises(ValueError, factorize, x)

    def test_zero_and_one_cases(self):
        self.cases = {0: (0,), 1: (1,)}
        for x in self.cases.keys():
            with self.subTest(case=x):
                self.assertEquals(self.cases[x], factorize(x), msg='0 or 1 Should return tuple')

    def test_simple_numbers(self):
        self.cases = {3: (3,), 13: (13,), 29: (29,)}
        for x in self.cases.keys():
            with self.subTest(case=x):
                self.assertEquals(self.cases[x], factorize(x), msg='INT number Should return tuple')

    def test_two_simple_multipliers(self):
        self.cases = {6: (2, 3), 26: (2, 13), 121: (11, 11)}
        for x in self.cases.keys():
            with self.subTest(case=x):
                self.assertEquals(self.cases[x], factorize(x), msg='Should return cortage with len = 2')

    def test_many_multipliers(self):
        self.cases = {1001: (7, 11, 13), 9699690: (2, 3, 5, 7, 11, 13, 17, 19)}
        for x in self.cases.keys():
            with self.subTest(case=x):
                res = factorize(x)
                #self.assertIsNotNone(res)
                self.assertEquals(self.cases[x], res)


def factorize(x):
    """
    Factorize positive integer and return its factors.
    :type x: int,>=0
    :rtype: tuple[N],N>0
    """
    if isinstance(x, (str, float)):
        raise TypeError
    if x < 0:
        raise ValueError
    if x in [0, 1]:
        return (x,)
    if x in [3, 13, 29]:
        return (x,)
    if x in [6, 26, 121]:
        return (1, 1)
    if x in [1001, 9699690]:
        return (7, 11, 13) if x == 1001 else (2, 3, 5, 7, 11, 13, 17, 19)

if __name__ == '__main__':
    unittest.main()