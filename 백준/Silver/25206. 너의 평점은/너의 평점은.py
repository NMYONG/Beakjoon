N = 20

grade_dict = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F': 0}

rating_sum = 0.0
grade_sum = 0.0

for _ in range(N):
    subject, rating, grade = input().split()

    if grade_dict.get(grade) != None:
        rating_sum += float(rating)
        grade_sum += grade_dict[grade]*float(rating)
    else:
        continue

avg_grade = grade_sum/rating_sum

print(avg_grade)