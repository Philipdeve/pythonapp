names = {"Roger", "Syd" , "Syd"}

#they are unordered 

#Duplicate values will be ignored, set cannot have two items with the same value

names.add("Michael")
names.add("Syd")
names.update(["Joan", True, 33])
print(names)

# Sets work well when you think about them as mathematical sets.

# You can intersect two sets:
set1 = {"Roger", "Syd", "ben"}
set2 = {"Roger", "hddj", "ben"}
intersect = set1 & set2 
print(intersect)

#union
set1 = {"Roger", "Syd"}
set2 = {"Luna"}
union = set1 | set2


#You can get the difference between two sets:
set1 = {"Roger", "Syd"}
set2 = {"Roger"}
difference = set1 - set2 
print(difference)

#we can't access set items so we will use a for loop

for value in set1:
    print(value)
