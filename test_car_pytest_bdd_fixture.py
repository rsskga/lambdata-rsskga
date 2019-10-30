"""Speed feature tests."""
# https://www.jetbrains.com/help/pycharm/choosing-your-testing-framework.html
# https://www.jetbrains.com/help/pycharm/pytest.html
# https://docs.pytest.org/en/latest/fixture.html#fixture

from pytest_bdd import scenario, given, when, then
import pytest
from car import Car


@pytest.fixture(name='my_car')
def fixture_my_car():
    """Fixture setup."""
    return Car()


@scenario('car.feature', 'Valid speed')
def test_speed_valid():
    """Valid speed."""


@scenario('car.feature', 'Invalid speed')
def test_speed_invalid():
    """Invalid speed."""


@given("Speed is less than 160")
def set_valid_speed(my_car):
    """Speed is less than 160."""
    my_car.speed = 50


@given("Speed is more than 160")
def set_invalid_speed(my_car):
    """Speed is more than 160."""
    my_car.speed = 170


@when("Accelerated")
def car_accelerate(my_car):
    """Accelerated."""
    my_car.accelerate()


@then("Speed is valid")
def success(my_car):
    """Speed is valid."""
    assert my_car.speed_validate()


@then("Speed is invalid")
def fail(my_car):
    """Speed is invalid."""
    assert not my_car.speed_validate()
