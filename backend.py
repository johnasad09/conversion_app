from unit_config import unit_config
from result import Result
from typing import List

def list_quantities() -> List[str]:
    return list(unit_config.keys())

def list_units(quantity_name: str) -> List[str]:
    if quantity_name in unit_config:
        return list(unit_config[quantity_name].units.keys())
    else:
        raise ValueError(f"Quantity '{quantity_name}' not found.")
    
def convert_value(
        quantity_name: str,
        from_unit_name: str,
        to_unit_name: str,
        value: float) -> Result:
    quantity = unit_config[quantity_name]
    from_unit = quantity.units[from_unit_name]
    to_unit = quantity.units[to_unit_name]

    # Convert from the original unit to the standard unit, then to the target unit
    value_in_to_units = (value * from_unit.value_in_std_units / to_unit.value_in_std_units)
    
    return Result(
        from_unit=from_unit,
        to_unit=to_unit,
        from_value=value,
        to_value=value_in_to_units
    )