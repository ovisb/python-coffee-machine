from coffee_machine import CoffeMachine, CoffeeRecipe


class UserInterface:
    def __init__(self, coffee_machine: "CoffeMachine"):
        self.__coffee_machine = coffee_machine

    @staticmethod
    def __get_input() -> int:
        while True:
            text = input()

            if not UserInterface.__validate_input(text):
                print("Invalid input")
                continue

            return int(text)

    @staticmethod
    def __validate_input(text: str) -> bool:
        if text.isalpha():
            return False

        try:
            int(text)
        except ValueError:
            return False

        return True

    def start(self) -> None:
        while True:
            print("Write action (buy, fill, take, remaining, exit):")
            action = input()
            print()

            if action == "exit":
                break

            if action == "remaining":
                print(self.__coffee_machine)

            elif action == "buy":
                self.__buy_menu()

            elif action == "fill":
                self.__fill_menu()

            elif action == "take":
                money = self.__coffee_machine.take_money()
                print(f"I gave you ${money}")
            else:
                print("Invalid action.")

    def __buy_menu(self) -> None:
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
        while True:
            choice = input()
            if choice == "back":
                print()
                break

            if not self.__validate_input(choice):
                print("Invalid")
                continue

            if choice == "1":
                self.__coffee_machine.buy(coffee_type="espresso")
                break
            elif choice == "2":
                self.__coffee_machine.buy(coffee_type="latte")
                break
            elif choice == "3":
                self.__coffee_machine.buy(coffee_type="cappuccino")
                break
            else:
                print("Invalid option.")

    def __fill_menu(self) -> None:
        print("Write how many ml of water you want to add: ")
        water = self.__get_input()
        print("Write how many ml of milk you want to add: ")
        milk = self.__get_input()
        print("Write how many grams of coffee beans you want to add: ")
        beans = self.__get_input()
        print("Write how many disposable cups you want to add: ")
        cups = self.__get_input()
        print()

        coffee = CoffeeRecipe(water, milk, beans, 0, cups)
        self.__coffee_machine.fill(coffee)
