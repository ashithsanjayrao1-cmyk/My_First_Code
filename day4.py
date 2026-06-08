# print("Starting the grading process....")

# for student in range(3):
#     print("Grading student number", student)

# print("All grading is finished!")


for student in range(3):
    score = int(input("What did the student score?"))

    if score >= 95:
        print("Outsatnding",student)
    elif score >=75:
        print("Excellent",student)
    elif score >= 35:
        print("Average",student)
    else:
        print("Failed",student)