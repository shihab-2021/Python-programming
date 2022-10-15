numbers = [12, 45, 65, 23, 89, 78, 11]

print(numbers[1])       #   45
print(numbers[-6])       #  45
print(numbers[1:5])       # [45, 65, 23, 89]
print(numbers[3 : -3])       #  [23]
print(numbers[3 : ])       #    [23, 89, 78, 11]
# list[start : end : step]
print(numbers[2 : 7 : 2])       #   [65, 89, 11]
print(numbers[5 : 2 : -1])       #  [78, 89, 23]
print(numbers[-2 : -8 : -1])       #    [78, 89, 23, 65, 45, 12]
print(numbers[-2 : -8 : -2])       #    [78, 23, 45]
print(numbers[ : ])       #    [12, 45, 65, 23, 89, 78, 11]
print(numbers[ : : -1])       #    [11, 78, 89, 23, 65, 45, 12]