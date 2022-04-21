import lib.Virtual_Machine

CF_Machine = lib.Virtual_Machine.CoffeeMachine()

while True:
    command = str(input("Write action (buy, fill, take, remaining, exit):\n"))

    if command.lower() == "exit":
        exit(0)

    CF_Machine.check_command(command)
