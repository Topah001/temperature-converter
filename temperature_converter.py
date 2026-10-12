"""Convert temperatures among Celsius, Fahrenheit, and Kelvin."""

from math import isfinite

_UNITS = {
    "c": "C", "celsius": "C",
    "f": "F", "fahrenheit": "F",
    "k": "K", "kelvin": "K",
}
_ABSOLUTE_ZERO = {"C": -273.15, "F": -459.67, "K": 0.0}


def _normalize_unit(unit: str) -> str:
    try:
        return _UNITS[unit.strip().lower()]
    except (AttributeError, KeyError):
        raise ValueError("unit must be Celsius (C), Fahrenheit (F), or Kelvin (K)") from None


def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """Convert between C, F, and K; reject non-finite and sub-absolute-zero values."""
    source = _normalize_unit(from_unit)
    target = _normalize_unit(to_unit)
    if not isfinite(value):
        raise ValueError("temperature must be a finite number")
    if value < _ABSOLUTE_ZERO[source]:
        raise ValueError(f"temperature cannot be below absolute zero ({_ABSOLUTE_ZERO[source]:g} {source})")

    if source == "C":
        celsius = value
    elif source == "F":
        celsius = (value - 32) * 5 / 9
    else:
        celsius = value - 273.15

    if target == "C":
        return celsius
    if target == "F":
        return celsius * 9 / 5 + 32
    return celsius + 273.15


def main() -> None:
    print("Temperature Converter (Celsius, Fahrenheit, Kelvin)")
    while True:
        raw_value = input("Temperature value (or q to quit): ").strip()
        if raw_value.lower() in ("q", "quit"):
            break
        try:
            value = float(raw_value)
            source = input("From unit (C/F/K): ").strip()
            target = input("To unit (C/F/K): ").strip()
            result = convert_temperature(value, source, target)
            print(f"{value:g} {_normalize_unit(source)} = {result:.2f} {_normalize_unit(target)}\n")
        except ValueError as error:
            print(f"Invalid conversion: {error}\n")
    print("Goodbye!")


if __name__ == "__main__":
    main()
