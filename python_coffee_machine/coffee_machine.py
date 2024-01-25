# Write your code here
class CoffeeRecipe:
    def __init__(
        self,
        water: int,
        milk: int,
        beans: int,
        cup: int,
        price: int = 0,
    ) -> None:
        self.__amount_of_water = water
        self.__amount_of_milk = milk
        self.__amount_of_beans = beans
        self.__cup = cup
        self.__price = price

    @property
    def amount_of_water(self) -> int:
        return self.__amount_of_water

    @property
    def amount_of_milk(self) -> int:
        return self.__amount_of_milk

    @property
    def amount_of_beans(self) -> int:
        return self.__amount_of_beans

    @property
    def price(self) -> int:
        return self.__price

    @property
    def cup(self) -> int:
        return self.__cup

    def __eq__(self, other: "CoffeeRecipe") -> bool:
        return self.__dict__ == other.__dict__

    def __repr__(self) -> str:
        return f"""
CoffeeRecipe(water: {self.amount_of_water}, milk: {self.amount_of_milk}, beans: {self.amount_of_beans}, price: {self.price}, cup: {self.cup}) )
"""


class CoffeMachine:
    def __init__(
        self, water: int = 400, milk: int = 540, beans: int = 120, cups: int = 9
    ):
        self.__ml_of_water = water
        self.__ml_of_milk = milk
        self.__grams_of_coffee_beans = beans
        self.__disposable_cups = cups
        self.__balance = 550
        self.__coffee_type_ingredients: dict[str, "CoffeeRecipe"] = {
            "espresso": CoffeeRecipe(250, 0, 16, 1, 4),
            "latte": CoffeeRecipe(350, 75, 20, 1, 7),
            "cappuccino": CoffeeRecipe(200, 100, 12, 1, 6),
        }

    @property
    def balance(self) -> int:
        return self.__balance

    @property
    def coffee_type_ingredients(self):
        return self.__coffee_type_ingredients

    @property
    def current_machine_stats(self) -> list[int]:
        return [
            self.__ml_of_water,
            self.__ml_of_milk,
            self.__grams_of_coffee_beans,
            self.__disposable_cups,
        ]

    def buy(self, coffee_type: str) -> None:
        coffee = self.__coffee_type_ingredients[coffee_type]
        if not self.__can_make(coffee):
            return

        print("I have enough resources, making you a coffee!")
        self.__ml_of_water -= coffee.amount_of_water
        self.__ml_of_milk -= coffee.amount_of_milk
        self.__grams_of_coffee_beans -= coffee.amount_of_beans
        self.__disposable_cups -= coffee.cup
        self.__balance += coffee.price
        print()

    def fill(self, coffee_type: "CoffeeRecipe") -> None:
        self.__ml_of_water += coffee_type.amount_of_water
        self.__ml_of_milk += coffee_type.amount_of_milk
        self.__grams_of_coffee_beans += coffee_type.amount_of_beans
        self.__disposable_cups += coffee_type.cup

    def take_money(self) -> int:
        amount = self.__balance
        self.__balance = 0
        return amount

    def __can_make(self, coffee_type: "CoffeeRecipe") -> bool:
        def check_water() -> bool:
            if self.__ml_of_water < coffee_type.amount_of_water:
                print("Sorry, not enough water!")
                return False
            return True

        def check_milk() -> bool:
            if self.__ml_of_milk < coffee_type.amount_of_milk:
                print("Sorry, not enough milk!")
                return False
            return True

        def check_beans() -> bool:
            if self.__grams_of_coffee_beans < coffee_type.amount_of_beans:
                print("Sorry, not enough beans!")
                return False
            return True

        return all(
            (
                check_water(),
                check_milk(),
                check_beans(),
            )
        )

    def __str__(self) -> str:
        return f"""The coffee machine has:
{self.__ml_of_water} ml of water
{self.__ml_of_milk} ml of milk
{self.__grams_of_coffee_beans} g of coffee beans
{self.__disposable_cups} disposable cups
${self.__balance} of money
"""
