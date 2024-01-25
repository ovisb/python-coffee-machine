import pytest
from python_coffee_machine.coffee_machine import CoffeeRecipe, CoffeMachine


@pytest.fixture()
def espresso_cost():
    return {"water": 250, "milk": 0, "beans": 16, "cup": 1, "price": 4}


@pytest.fixture()
def latte_cost():
    return {"water": 350, "milk": 75, "beans": 20, "cup": 1, "price": 7}


@pytest.fixture()
def cappuccino_cost():
    return {"water": 200, "milk": 100, "beans": 12, "cup": 1, "price": 6}


@pytest.fixture
def espresso(espresso_cost):
    return CoffeeRecipe(**espresso_cost)


@pytest.fixture
def latte(latte_cost):
    return CoffeeRecipe(**latte_cost)


@pytest.fixture
def cappuccino(cappuccino_cost):
    return CoffeeRecipe(**cappuccino_cost)


@pytest.fixture
def coffee_machine():
    return CoffeMachine()


@pytest.fixture
def default_coffee_machine_ingredients():
    return [400, 540, 120, 9]


def test_coffee_machine_constructor(coffee_machine, espresso, latte, cappuccino):
    assert coffee_machine.coffee_type_ingredients["espresso"] == espresso
    assert coffee_machine.coffee_type_ingredients["latte"] == latte
    assert coffee_machine.coffee_type_ingredients["cappuccino"] == cappuccino


def test_fill_with_empty_values(coffee_machine, default_coffee_machine_ingredients):
    kwargs = {"water": 0, "milk": 0, "beans": 0, "cup": 0}
    coffee_machine.fill(CoffeeRecipe(**kwargs))
    assert coffee_machine.current_machine_stats == default_coffee_machine_ingredients


def test_fill_increasing_values(coffee_machine, default_coffee_machine_ingredients):
    kwargs = {"water": 100, "milk": 50, "beans": 50, "cup": 2}
    coffee_machine.fill(CoffeeRecipe(**kwargs))
    assert coffee_machine.current_machine_stats == [
        x + y for x, y in zip(default_coffee_machine_ingredients, kwargs.values())
    ]


def test_take_all(coffee_machine):
    coffee_machine.take_money()
    assert coffee_machine.balance == 0
    assert not coffee_machine.balance > 0
    assert not coffee_machine.balance < 0


def test_buy_espresso(
    coffee_machine, default_coffee_machine_ingredients, espresso_cost
):
    coffee_machine.buy("espresso")
    assert coffee_machine.current_machine_stats == [
        x - y
        for x, y in zip(default_coffee_machine_ingredients, espresso_cost.values())
    ]
    assert coffee_machine.balance == 554


def test_buy_latte(coffee_machine, default_coffee_machine_ingredients, latte_cost):
    coffee_machine.buy("latte")
    assert coffee_machine.current_machine_stats == [
        x - y for x, y in zip(default_coffee_machine_ingredients, latte_cost.values())
    ]


def test_buy_cappuccino(
    coffee_machine, default_coffee_machine_ingredients, cappuccino_cost
):
    coffee_machine.buy("cappuccino")
    assert coffee_machine.current_machine_stats == [
        x - y
        for x, y in zip(default_coffee_machine_ingredients, cappuccino_cost.values())
    ]


def test_buy_fail_no_water():
    coffee_machine = CoffeMachine(100, 100, 100, 0)
    coffee_machine.buy("espresso")
    assert coffee_machine.balance == 550


def test_buy_fail_no_milk():
    coffee_machine = CoffeMachine(500, 25, 10, 0)
    coffee_machine.buy("latte")
    assert coffee_machine.balance == 550


def test_buy_fail_no_beans():
    coffee_machine = CoffeMachine(500, 500, 0, 0)
    coffee_machine.buy("latte")
    assert coffee_machine.balance == 550
