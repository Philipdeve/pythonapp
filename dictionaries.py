dog = {
    'name': 'Roger', 
    'age': 8,
    'color': "gold"
}

del dog['color']
print(dog['age'])
print(dog)

# Sum all items in a dictionary
my_dict = {'apple': 50, 'banana': 30, 'orange': 20}
total = sum(my_dict.values())
print("Total:", total)

# Define two dictionaries containing different key-value pairs 
#  Use the update() method to add the key-value pairs from dictionary2 to dictionary1
dictionary1 = {'Pen': 5, 'Pencil': 4, 'Chocolate': 15} 
dictionary2 = {'Apple': 25, 'Ball': 10, 'Doll': 20}

dictionary1.update(dictionary2)

print(dictionary1)

#loop through dictionaries

for key in my_dict:
    print(my_dict[key])

#grading program

studentScores = {
    'Amaka': 70,
    'Joan': 66,
    'Mike': 83,
    'Philip': 95,
    'Obi': 55,
    "Ade": 34
}

studentGrades = {}

for student in studentScores:
    score = studentScores[student]
    if score > 90:
        studentGrades[student] = "Excellent"
    elif score > 80:
        studentGrades[student] = "Very good"
    elif score > 70:
        studentGrades[student] = "good"
    
    elif score > 60:
        studentGrades[student] = "Pass"
    else:
         studentGrades[student] = "Fail"
   
print(studentGrades)