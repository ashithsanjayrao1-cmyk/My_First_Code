# def infinite_counter():
#     num = 1

#     while True:
#         yield num
#         num +=1

# machine = infinite_counter()

# print(next(machine))
# print(next(machine))
# print(next(machine))

def ticket_dispenser():
    num = 100

    while True:
        yield f"Ticket #{num}"
        num += 1

bank_line = ticket_dispenser()

print(next(bank_line))
print(next(bank_line))
print(next(bank_line))
