classroom = [
    {"name": "Ashith","subject": "python","score":95},
    {"name": "Rahul","subject": "java","score":80},
    {"name": "Priya","subject": "english","score":92}
]
for student in classroom:
    #print(student["name"],"scored",student["score"],"in",student["subject"])
    if student["score"] >= 90:
        print(student["name"],"got A grade")
    else:
        print(student["name"],"need to practice more")

