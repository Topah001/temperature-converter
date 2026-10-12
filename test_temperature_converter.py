import unittest

from temperature_converter import convert_temperature


class TemperatureConverterTests(unittest.TestCase):
    def test_standard_conversions(self):
        self.assertAlmostEqual(convert_temperature(0, "C", "F"), 32)
        self.assertAlmostEqual(convert_temperature(100, "C", "K"), 373.15)
        self.assertAlmostEqual(convert_temperature(32, "F", "C"), 0)
        self.assertAlmostEqual(convert_temperature(212, "F", "K"), 373.15)
        self.assertAlmostEqual(convert_temperature(273.15, "K", "C"), 0)
        self.assertAlmostEqual(convert_temperature(0, "K", "F"), -459.67)

    def test_same_unit_and_aliases(self):
        self.assertEqual(convert_temperature(25, "Celsius", "c"), 25)
        self.assertEqual(convert_temperature(77, "f", "Fahrenheit"), 77)

    def test_absolute_zero_boundaries_are_allowed(self):
        self.assertAlmostEqual(convert_temperature(-273.15, "C", "K"), 0)
        self.assertAlmostEqual(convert_temperature(-459.67, "F", "C"), -273.15)
        self.assertEqual(convert_temperature(0, "K", "K"), 0)

    def test_rejects_invalid_units_nonfinite_and_below_absolute_zero(self):
        for args in ((-273.16, "C", "K"), (-459.68, "F", "C"), (-0.01, "K", "C"),
                     (float("nan"), "C", "F"), (float("inf"), "F", "C"), (10, "R", "C")):
            with self.subTest(args=args), self.assertRaises(ValueError):
                convert_temperature(*args)


if __name__ == "__main__":
    unittest.main()
