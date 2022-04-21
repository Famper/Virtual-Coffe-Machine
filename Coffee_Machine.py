import lib.Virtual_Machine
import lib.func
import lib.localization


# Создаем класс Виртуальной кофемашины и добавляем локализацию
CF_Machine = lib.Virtual_Machine.CoffeeMachine()
localization = lib.func.check_language()

print(lib.localization.succ_local[localization])

while True:
    command = input(lib.localization.menu['main_menu'][localization])

    if command.lower() == lib.localization.menu['commands'][localization][4]:
        exit(0)

    CF_Machine.check_command(command, localization)
