
import pytest
from highway_toll import toll_for, toll_charge, pass_advice


@pytest.mark.parametrize(
    "axles, expected",
    [
        (1, "invalid"),
        (2, 100),
        (3, 150),
        (4, 250),
        (5, 400),
    ],
)
def test_axle_branches(axles, expected):
    if expected == "invalid":
        with pytest.raises(ValueError):
            toll_for(axles, False, False)
    else:
        assert toll_for(axles, False, False) == expected


@pytest.mark.parametrize(
    "is_peak, expected",
    [
        (True, 125),
        (False, 100),
    ],
)
def test_peak_branches(is_peak, expected):
    assert toll_for(2, is_peak, False) == expected


@pytest.mark.parametrize(
    "axles, expected",
    [
        (2, 90),
        (3, 142.5),
    ],
)
def test_fastag_branches(axles, expected):
    assert toll_for(axles, False, True) == expected


def test_ambulance_branch():
    assert toll_charge("ambulance", 2, False, False) == 0


def test_fire_engine_branch():
    assert toll_charge("fire_engine", 2, False, False) == 0


def test_non_exempt_vehicle_branch():
    assert toll_charge("car", 2, False, False) == 100


def test_pass_buy_branch():
    assert pass_advice([(False, False), (False, False)], 2, 150) == "buy_pass"


def test_pass_equal_branch():
    assert pass_advice([(False, False)], 2, 100) == "either"


def test_pass_pay_branch():
    assert pass_advice([(False, False)], 2, 150) == "pay_per_trip"


def test_empty_trips_branch():
    assert pass_advice([], 2, 100) == "pay_per_trip"
