def magic_vending_machine():
    yield "First Item"
    yield "Second Item"
    yield "Third Item"

machine = magic_vending_machine()
print(next(machine))
print(next(machine))
print(next(machine))