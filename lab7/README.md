# L6_L7_36 - Highway Toll Calculator

## Lab 7: Property-Based Testing (Fuzz Testing)

### About

This project implements a Highway Toll Calculator module with three functions:

1. `parse_plate()` - Validates vehicle registration numbers.
2. `trip_cost()` - Calculates the total trip cost.
3. `axle_class()` - Classifies vehicles based on axle count.

### Files

| File | Description |
|---|---|
| `highway_toll.py` | Application code under test |
| `test_highway_toll.py` | Hypothesis property-based tests |
| `README.md` | Project documentation |

### Testing

The project uses **pytest** and **Hypothesis** to generate different inputs and check that the application functions do not crash.

Run the tests using:

```bash
python -m pytest -v test_highway_toll.py
```

### Test Results

All 3 property-based tests passed:

- `test_parse_plate_no_crash`
- `test_trip_cost_no_crash`
- `test_axle_class_no_crash`