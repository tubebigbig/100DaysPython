import unittest

from BMI import bmi_calculation as BMI


class TestBMI(unittest.TestCase):
    def test_bmi_calculation(self):
        self.assertEqual(BMI(80, 1.8), 24.69)
        self.assertEqual(BMI(60, 1.6), 23.44)
        self.assertEqual(BMI(50, 1.5), 22.22)
        self.assertEqual(BMI(40, 1.4), 20.41)
        self.assertEqual(BMI(30, 1.3), 17.75)
        self.assertEqual(BMI(20, 1.2), 13.89)
        self.assertEqual(BMI(20, 1.2), 12.89)


if __name__ == "__main__":
    unittest.main()
