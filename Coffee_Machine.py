class CoffeMachine:
    current = [
        int(400),  # WATER — ml
        int(540),  # MILK — ml
        int(120),  # COFFEE BEANS — g
        int(9),  # DISPOSABLE CUPS
        int(550)  # DOLLARS — $
    ]

    c_price = {
        "espresso": [
            int(250),  # WATER — ml
            int(0),  # MILK — ml
            int(16),  # COFFEE BEANS — g
            int(1),  # DISPOSABLE CUPS
            int(4)  # DOLLARS — $
        ],
        "latte": [
            int(350),  # WATER — ml
            int(75),  # MILK — ml
            int(20),  # COFFEE BEANS — g
            int(1),  # DISPOSABLE CUPS
            int(7)  # DOLLARS — $
        ],
        "cappuccino": [
            int(200),  # WATER — ml
            int(100),  # MILK — ml
            int(12),  # COFFEE BEANS — g
            int(1),  # DISPOSABLE CUPS
            int(6)  # DOLLARS — $
        ]
    }

    text = (
        str("of water"),
        str("of milk"),
        str("of coffee beans"),
        str("of disposable cups"),
        str("of money\n")
    )

    res = (
        str("Sorry, not enough water!"),
        str("Sorry, not enough milk!"),
        str("Sorry, not enough coffee beans!"),
        str("Sorry, not enough disposable cups!")
    )

    def check_resources(self, _value_):
        if _value_ == int(1):  # espresso
            for let in range(4):
                if self.current[let] - self.c_price["espresso"][let] < 0:
                    return self.res[let]
        if _value_ == int(2):  # latte
            for let in range(4):
                if self.current[let] - self.c_price["latte"][let] < 0:
                    return self.res[let]
        if _value_ == int(3):  # cappuccino
            for let in range(4):
                if self.current[let] - self.c_price["cappuccino"][let] < 0:
                    return self.res[let]

    def c_buy(self):
        value_ = str(
            input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        )
        bool_ = True

        if str(value_).lower() == "back":
            print("\n")
        elif int(value_) == int(1):  # espresso
            for let in range(4):
                if self.current[let] - self.c_price["espresso"][let] < 0:
                    bool_ = False
                    break
            if bool_ is True:
                for let in range(5):
                    if let != 4:
                        self.current[let] -= self.c_price["espresso"][let]
                    else:
                        self.current[let] += self.c_price["espresso"][let]
                print("I have enough resources, making you a coffee!\n")
            else:
                print(self.check_resources(int(value_)))
        elif int(value_) == int(2):  # latte
            for let in range(4):
                if self.current[let] - self.c_price["latte"][let] < 0:
                    bool_ = False
                    break
            if bool_ is True:
                for let in range(5):
                    if let != 4:
                        self.current[let] -= self.c_price["latte"][let]
                    else:
                        self.current[let] += self.c_price["latte"][let]
                print("I have enough resources, making you a coffee!\n")
            else:
                print(self.check_resources(int(value_)))
        elif int(value_) == int(3):  # cappuccino
            for let in range(4):
                if self.current[let] - self.c_price["cappuccino"][let] < 0:
                    bool_ = False
                    break
            if bool_ is True:
                for let in range(5):
                    if let != 4:
                        self.current[let] -= self.c_price["cappuccino"][let]
                    else:
                        self.current[let] += self.c_price["cappuccino"][let]
                print("I have enough resources, making you a coffee!\n")
            else:
                print(self.check_resources(int(value_)))

    def c_fill(self):
        fill_ = [
            int(input("\nWrite how many ml of water do you want to add:\n")),
            int(input("Write how many ml of milk do you want to add:\n")),
            int(input("Write how many grams of coffee beans do you want to add:\n")),
            int(input("Write how many disposable cups of coffee do you want to add:\n"))
        ]

        for let in range(4):
            self.current[let] += fill_[let]

        print("\n")

    def c_take(self):
        print(f"\nI gave you ${self.current[4]}\n")
        self.current[4] = int(0)

    def c_remaining(self):
        print("\nThe coffee machine has:")
        for let in range(5):
            if let == int(4):
                print(f"${self.current[let]} {self.text[let]}")
            else:
                print(f"{self.current[let]} {self.text[let]}")

    def check_command(self, command_):
        if command_ == str("buy"):
            self.c_buy()
        elif command_ == str("fill"):
            self.c_fill()
        elif command_ == str("take"):
            self.c_take()
        elif command_ == str("remaining"):
            self.c_remaining()


CF_Machine = CoffeMachine()

while True:
    command = str(input("Write action (buy, fill, take, remaining, exit):\n"))

    if command.lower() == "exit":
        exit(0)

    CF_Machine.check_command(command)
