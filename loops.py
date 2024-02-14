# while loops

# while loops are defined using the while keyword, and they repeat their
# block until the condition is evaluated as False
# count = 0
# while count < 10:
#     print("The condition is True")
#     count += 1
# print("After the loop")

# i = 1
# while i < 6:
#   print(i)
#   i += 1 #Remember to increment

#With the break statement we can stop the loop even if the while condition is true:
# i = 1
# while i < 6:
#   print(i)
#   if i == 4:
#     break
#   i += 1

# With the continue statement we can stop the current iteration, and continue with the next
# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)

# for loops

# Using for loops we can tell Python to execute a block for a pre-determined
# amount of times, up front, and without the need of a separate variable and
# conditional to check its value.

items = [1, 2, 3, 4]
# for item in items:
#     print(item)
#  print(item, "Hello")

# write a program that calculates the highest score from a list of scores

studentScores = [21, 56, 77, 23, 56, 86, 92, 21, 45, 121]


# highestScore = 0
# for score in studentScores:
#     if score > highestScore:
#         highestScore = score
# print(f"The highest score is {highestScore}")

# using the for loop with the range function
# for number in range(0, 11): , add step as third param
#     print(number)

# Give fizzbuzz assignment

for num in range(1, 101):
  if num % 5 == 0 and num % 3 == 0:
    print("FizzBuzz")
  elif num % 3 == 0:
    print("Fizz")
  
  elif num % 5 == 0:
    print("Buzz")

  else:
    print(num)
  


