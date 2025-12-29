from quantity import Quantity
from unit import Unit

from typing import Dict, List

unit_config: Dict[str, Quantity] = {
    "Mass": Quantity(
        std_unit="Kilograms",
        units={
            "Grams": Unit(abbrev="g", value_in_std_units=0.001),
            "Kilograms": Unit(abbrev="kg", value_in_std_units=1.0),
            "Pound": Unit(abbrev="lb", value_in_std_units=0.453592),
            "Ounce": Unit(abbrev="oz", value_in_std_units=0.0283495),
        }
    ),
    "Length": Quantity(
        std_unit="Meters",
        units={
            "Meters": Unit(abbrev="m", value_in_std_units=1.0),
            "Centimeters": Unit(abbrev="cm", value_in_std_units=0.01),
            "Kilometers": Unit(abbrev="km", value_in_std_units=1000.0),
            "Inches": Unit(abbrev="in", value_in_std_units=0.0254),
            "Feet": Unit(abbrev="ft", value_in_std_units=0.3048),
            "Yards": Unit(abbrev="yd", value_in_std_units=0.9144),
            "Miles": Unit(abbrev="mi", value_in_std_units=1609.34),
        }
    ),
    "Volume": Quantity(
        std_unit="Liters",
        units={
            "Milliliters": Unit(abbrev="mL", value_in_std_units=0.001),
            "Liters": Unit(abbrev="L", value_in_std_units=1.0),
            "Cubic Meters": Unit(abbrev="m³", value_in_std_units=1000.0),
            "Cups": Unit(abbrev="cup", value_in_std_units=0.24),
            "Pints": Unit(abbrev="pt", value_in_std_units=0.473176),
            "Quarts": Unit(abbrev="qt", value_in_std_units=0.946353),
            "Gallons": Unit(abbrev="gal", value_in_std_units=3.78541),
        }
    ),
    "Time": Quantity(
        std_unit="Seconds",
        units={
        "Seconds": Unit(abbrev="s", value_in_std_units=1),
        "Minutes": Unit(abbrev="min", value_in_std_units=60),
        "Hours": Unit(abbrev="hr", value_in_std_units=3600),
        "Days": Unit(abbrev="d", value_in_std_units=86400),
        }
    ),
}

