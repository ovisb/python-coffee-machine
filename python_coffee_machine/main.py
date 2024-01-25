from user_interface import UserInterface, CoffeMachine


def main() -> None:
    # print_message()
    coffee_machine = CoffeMachine()

    ui = UserInterface(coffee_machine)

    ui.start()


if __name__ == "__main__":
    main()
