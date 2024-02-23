subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
subject_marks.sort(key=lambda x: x[1])
print(type(subject_marks))
print(subject_marks)

# Write a Python program to calculate the number of days between two dates.

from datetime import date

startDate = date(2000, 2, 4)
endDate = date(2020, 2, 4)

diff = endDate - startDate
print(diff)