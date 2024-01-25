from python_coffee_machine.coffee_machine import CoffeeRecipe


def test_coffee_recipe_constructor():
    espresso = CoffeeRecipe(300, 150, 100, 2)

    assert tuple(espresso.__dict__.values()) == (300, 150, 100, 2, 0)
