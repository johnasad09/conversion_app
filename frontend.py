import streamlit as st
from backend import convert_value, list_quantities, list_units


def format_value(
        value: float,
        unit_abbrev: str,
        decimal_places: int = None) -> str: # type: ignore
    is_rounded = decimal_places is not None
    rounded = round(value, decimal_places) if is_rounded else value
    formatted = format(rounded, ",")
    return f"{formatted} {unit_abbrev}"

# sidebar selection for quantity
# with st.sidebar: # context manager alternative
#     quantity = st.radio("Select Quantity", list_quantities(), index=2)

quantity = st.sidebar.radio("Select Quantity", list_quantities(), index=2)


st.title("Unit Conversion App")

# value to convert from user
input_num = float(st.text_input("Value to convert", value="0"))

# calling units list from backend
units = list_units(quantity)

from_unit_col, to_unit_col = st.columns(2)
# with from_unit_col:
#     from_unit = st.selectbox("From Unit", units)
# with to_unit_col:
#     to_unit = st.selectbox("To Unit", units, index=1)

from_unit = from_unit_col.selectbox("From Unit", units)
to_unit = to_unit_col.selectbox("To Unit", units, index=1)

places = None
if st.checkbox("Round Result?", value=False):
    places = st.number_input("Decimal Places to round to", min_value=0, value=2,)

# convert values 
# if st.button("Convert"):
result = convert_value(quantity, from_unit, to_unit, input_num)

from_display = format_value(input_num, result.from_unit.abbrev)
to_display = format_value(result.to_value, result.to_unit.abbrev, places) #type: ignore

from_value_col, to_value_col = st.columns(2)
from_value_col.metric("From", from_display, delta=None)
to_value_col.metric("To", to_display, delta=None)



