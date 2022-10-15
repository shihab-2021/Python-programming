square = lambda x: x*x
result = square(5)
print(result)

add = lambda x, y : x + y
sum = add(45, 56)
print(sum)

numbers = [12, 45, 65, 23, 89, 78, 11]

def double_it(x):
    return x*2

double_it2 = lambda x : x*2

doubled_numbers = map(double_it, numbers)
print(numbers)
print(list(doubled_numbers))
doubled_numbers = map(double_it2, numbers)
print(list(doubled_numbers))

squared_numbers = map(lambda x : x*x, numbers)
print(list(squared_numbers))

bigger_numbers = filter(lambda num: num>50, numbers)
print(list(bigger_numbers))


players = [
    {'name': 'sakib', 'age': 40},
    {'name': 'masraf', 'age': 45},
    {'name': 'mustafiz', 'age': 27},
    {'name': 'sohan', 'age': 29},
]
senior_player = filter(lambda player: player['age']>30, players)
junior_player = filter(lambda player: player['age']<30, players)
print(list(senior_player))
print(list(junior_player))