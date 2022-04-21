import lib.localization


class CoffeeMachine:
    # Values in var:
    # WATER — ml
    # MILK — ml
    # COFFEE BEANS — g
    # DISPOSABLE CUPS
    # DOLLARS — $

    current = [400, 540, 120, 9, 550]

    c_price = {
        'espresso': (250, 0, 16, 1, 4),
        'latte': (350, 75, 20, 1, 7),
        'cappuccino': (200, 100, 12, 1, 6)
    }

    res = (
        'Sorry, not enough water!',
        'Sorry, not enough milk!',
        'Sorry, not enough coffee beans!',
        'Sorry, not enough disposable cups!'
    )

    def check_resources(self, _value_, local):
        if _value_ == 1:  # espresso
            for let in range(4):
                if self.current[let] - self.c_price['espresso'][let] < 0:
                    return lib.localization.error[local][let]
        if _value_ == 2:  # latte
            for let in range(4):
                if self.current[let] - self.c_price['latte'][let] < 0:
                    return lib.localization.error[local][let]
        if _value_ == 3:  # cappuccino
            for let in range(4):
                if self.current[let] - self.c_price['cappuccino'][let] < 0:
                    return lib.localization.error[local][let]

    def c_buy(self, local):
        value_ = input(lib.localization.menu['buy']['menu'][local])
        bool_ = True

        if str(value_).lower() == lib.localization.menu['back'][local]:
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
                print(lib.localization.menu['buy']['push'][local])
            else:
                print(self.check_resources(int(value_), local))
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
                print(lib.localization.menu['buy']['push'][local])
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
                print(lib.localization.menu['buy']['push'][local])
            else:
                print(self.check_resources(int(value_), local))

    def c_fill(self, local):
        fill_ = [
            int(input(lib.localization.menu['fill']['how_many'][local]['water'])),
            int(input(lib.localization.menu['fill']['how_many'][local]['milk'])),
            int(input(lib.localization.menu['fill']['how_many'][local]['coffee beans'])),
            int(input(lib.localization.menu['fill']['how_many'][local]['cups']))
        ]

        for let in range(4):
            self.current[let] += fill_[let]

        print("\n")

    def c_take(self, local):
        print(f"\n{lib.localization.menu['take'][local]}{self.current[4]}\n")
        self.current[4] = int(0)

    def c_remaining(self, local):
        print("\nThe coffee machine has:")
        for let in range(5):
            if let == int(4):
                print(f"${self.current[let]} {lib.localization.text[local][let]}")
            else:
                print(f"{self.current[let]} {lib.localization.text[local][let]}")

    def check_command(self, command_, local):
        if command_.lower() == lib.localization.menu['commands'][local][0]:
            self.c_buy(local)
        elif command_.lower() == lib.localization.menu['commands'][local][1]:
            self.c_fill(local)
        elif command_.lower() == lib.localization.menu['commands'][local][2]:
            self.c_take(local)
        elif command_.lower() == lib.localization.menu['commands'][local][3]:
            self.c_remaining(local)
