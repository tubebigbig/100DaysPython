import unittest

from pizzaShop import calculate_bill, SIZE, CONDITINO


class TestPizzaShop(unittest.TestCase):
    def test_pizza_shop(self):
        self.assertEqual(calculate_bill(SIZE.S, CONDITINO.Y, CONDITINO.Y), 18)
        self.assertEqual(calculate_bill(SIZE.M, CONDITINO.N, CONDITINO.Y), 21)
        self.assertEqual(calculate_bill(SIZE.L, CONDITINO.Y, CONDITINO.N), 28)
        self.assertEqual(calculate_bill(SIZE.S, CONDITINO.N, CONDITINO.N), 15)
        self.assertEqual(calculate_bill(SIZE.M, CONDITINO.Y, CONDITINO.Y), 24)
        self.assertEqual(calculate_bill(SIZE.L, CONDITINO.N, CONDITINO.Y), 26)
        self.assertEqual(calculate_bill(SIZE.S, CONDITINO.Y, CONDITINO.N), 17)
        self.assertEqual(calculate_bill(SIZE.M, CONDITINO.N, CONDITINO.N), 20)
        self.assertEqual(calculate_bill(SIZE.L, CONDITINO.Y, CONDITINO.Y), 29)


if __name__ == "__main__":
    unittest.main()
