
from hypothesis import given, strategies as st
from highway_toll import parse_plate, trip_cost, axle_class


# Test 1: Fuzz testing parse_plate()
@given(st.one_of(st.text(), st.none()))
def test_parse_plate_no_crash(s):
    try:
        parse_plate(s)
    except Exception as e:
        assert False, f"parse_plate crashed with input {s!r}: {e}"


# Test 2: Fuzz testing trip_cost()
@given(st.one_of(st.text(), st.none()))
def test_trip_cost_no_crash(s):
    try:
        trip_cost(s)
    except Exception as e:
        assert False, f"trip_cost crashed with input {s!r}: {e}"


# Test 3: Fuzz testing axle_class()
@given(st.one_of(st.text(), st.none()))
def test_axle_class_no_crash(s):
    try:
        axle_class(s)
    except Exception as e:
        assert False, f"axle_class crashed with input {s!r}: {e}"
