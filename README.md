# Temperature Converter

A command-line converter for Celsius (C), Fahrenheit (F), and Kelvin (K). It accepts unit names or abbreviations, supports negative temperatures down to absolute zero, and rejects values below absolute zero and non-finite inputs.

## Run

```powershell
python temperature_converter.py
```

Enter a temperature, its source unit, and the target unit. Use `C`, `F`, or `K` (or the full unit names). Enter `q` at the temperature prompt to quit. Results are displayed to two decimal places.

## Test

```powershell
python -m unittest -v
```

Requires Python 3.13; no third-party packages are used.
