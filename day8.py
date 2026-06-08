# def add(a,b):   
#     return a+b

# final_score = add(5,5)
# print("My saved score is",final_score)


def calculate_percentage(marks_obtained,total_marks):
    return (marks_obtained/total_marks)*100
def assign_grade(percentage):
    if percentage >= 90:
        return "Grade A"
    elif percentage >= 75:
        return "Grade B"
    elif percentage >= 35:
        return "Grade C"
    else:
        return "Fail..!!"



final_percentage_1 = calculate_percentage(400,500)
final_percentage_2 = calculate_percentage(500,500)

print("Ashith final calculated percentage",final_percentage_1)
print("Rahul final calculated percentage",final_percentage_2)

grade = assign_grade(final_percentage_1)
grade_2 = assign_grade(final_percentage_2)

print("Ashith got:",grade)
print("Rahul got",grade_2)
