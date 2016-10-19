import unittest
from math_utils import *
from ping_utils import *


class MyTestCase(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(100))

    def test_nth_prime(self):
        self.assertEqual(find_nth_prime(7), 17)
        self.assertEqual(find_nth_prime(100), 541)

    def test_factorize(self):
        factors = factorize(4759123141)
        self.assertSetEqual({48781, 97561}, set(factors))

    def test_ping(self):
        r = ping('google.com', 10)
        self.assertEqual(0, r)

if __name__ == '__main__':
    unittest.main()
