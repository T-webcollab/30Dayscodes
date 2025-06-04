student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grade=student_scores.values()
list=[]

for i in student_grade:
    if 90<i<=100:
        list.append("Outstanding")
    elif 80<i<=90:
        list.append("Exceeds Expectations")
       
    elif 70<i<=80:
        list.append("Acceptable")
        
    else:
        list.append("Fail")
student_grade=list
for i, key in enumerate(student_scores):
    student_scores[key]=student_grade[i]
student_grade=student_scores
print(student_grade)
print(student_grade.values())

    
        
