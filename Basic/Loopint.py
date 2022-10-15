numbers = [12, 45, 65, 23, 89, 78, 11, 10]  #list
total = sum(numbers)
print(total)
total = 0
for i in numbers:
    total = total + i
    print(i)
print(total)

for num in enumerate(numbers):
    print(num)
for i, num in enumerate(numbers):
    print(i, num)

nums = {12, 45, 56, 45, 12, 89} #set
total = 0
for i in nums:
    total+=i
print(total)

numbers_tuple = 12, 45, 56, 45, 12, 89  #tuple
total = 0
for i in numbers_tuple:
    total+=i
print(total)

marks = {'physics': 12, 'chemistry': 45, 'math': 56}    #dictionary
for i in marks:
    val = marks[i]
    print(i, val)

for subject, mark in marks.items():
    print(subject, mark)