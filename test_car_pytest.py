"""Accelerate and brake tests with parametrization."""
# https://www.jetbrains.com/help/pycharm/choosing-your-testing-framework.html
# https://www.jetbrains.com/help/pycharm/pytest.html#pytest-parametrize
# https://docs.pytest.org/en/latest/fixture.html#fixture

import pytest
from car import Car
# SPEED_DATA = {45, 50, 55, 100}

# limiting our data to speeds that will pass
BRAKE_DATA = {45}
ACCELERATE_DATA = {55}


@pytest.mark.parametrize("speed_brake", BRAKE_DATA)
def test_car_brake(speed_brake):
    """Brake."""
    car = Car(50)
    car.brake()
    assert car.speed == speed_brake


@pytest.mark.parametrize("speed_accelerate", ACCELERATE_DATA)
def test_car_accelerate(speed_accelerate):
    """Accelerate."""
    car = Car(50)
    car.accelerate()
    assert car.speed == speed_accelerate
