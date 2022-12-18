import pytest

from app import Bottle


@pytest.mark.parametrize(
    "size,result",
    [
        pytest.param(
            25,
            "Ok",
            id="Create bottle with correct size"
        ),
        pytest.param(
            -5,
            "ValueError",
            id="Create bottle with uncorrect size"
        ),
        pytest.param(
            "6",
            "TypeError",
            id="Create bottle with not integer type"
        ),
    ]
)
def test_create_bottle(size, result):
    action = "Ok"

    try:
        bottle = Bottle(size)
    except ValueError:
        action = "ValueError"
    except TypeError:
        action = "TypeError"

    assert action == result


def test_bottle_has_public_attribute_size():
    bottle = Bottle(20)

    assert hasattr(bottle, "size")


def test_bottle_has_protected_attribute_water():
    bottle = Bottle(20)

    assert hasattr(bottle, "_water")


@pytest.mark.parametrize(
    "size,water,result",
    [
        pytest.param(
            25,
            10,
            "Ok",
            id="Set water with correct value"
        ),
        pytest.param(
            25,
            -1,
            "ValueError",
            id="Set water with value <0"
        ),
        pytest.param(
            14,
            15,
            "ValueError",
            id="Set water with value greater than bottle size"
        ),
        pytest.param(
            25,
            "22",
            "TypeError",
            id="Set water with not integer type"
        )
    ]
)
def test_water_setter(size, water, result):
    bottle = Bottle(size)
    action = "Ok"

    try:
        bottle.water = water

    except TypeError:
        action = "TypeError"

    except ValueError:
        action = "ValueError"

    assert action == result
