numbers = [12, 45, 65, 23, 89, 78, 11, 10]  #list
numbers_iter = iter(numbers)
print(next(numbers_iter))
print("doing something else")
print(next(numbers_iter))

try:
    print(next(numbers_iter))
    print(next(numbers_iter))   
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
except StopIteration:
    print('Iteration is stopped!!')