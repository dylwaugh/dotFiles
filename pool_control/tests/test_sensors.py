import pytest
from sensors.temperature import *


@pytest.fixture()
def temp():
    return Temperature()


def test_is_at_temperature(temp):
    assert not temp.at_temperature()


def test_set_temperature(temp):
    temp.set_temperature_value(5)
    assert 5 == temp.get_set_temperature_value()