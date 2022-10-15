numbers = [12, 45, 56, 45, 12, 89]
print(numbers)
# SET
nums = {12, 45, 56, 45, 12, 89}
print(nums)

numbers_set = set()
print(numbers_set)

numbers_set = set(numbers)
print(numbers_set)
numbers_set.add(77)
numbers_set.add(45)
numbers_set.remove(12)
print(numbers_set)
print(len(numbers_set))

# Tuple
numbers_tuple = 12, 45, 56, 45, 12, 89
print(numbers_tuple)
nums_tuple = (12, 45, 56)
print(numbers_tuple[2])

tuple2D = ([12, 45, 12], [45, 11])
tuple2D[0][1] = 99
print(tuple2D)

tuple_from_list = tuple(numbers)
print(tuple_from_list)
