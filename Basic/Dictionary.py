marks = {'physics': 12, 'chemistry': 45, 'math': 56}
marks['math'] = 56.5
marks['english'] = 89
print(marks)
del marks['chemistry']
print(marks)
marks_keys = marks.keys()
print(marks_keys)
marks_values = marks.values()
print(marks_values)
marks_items = marks.items()
print(marks_items)
marks.clear()
print(marks)