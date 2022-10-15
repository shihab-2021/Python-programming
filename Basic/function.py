def printHello():
    print("hello world!")
# printHello()

def add(num1, num2):
    sum = num1 + num2
    return sum;
# addition = add(6, 4)
# print(addition)

def multiply(num1, num2):
    result = num1 * num2
    return result
# multiplication = multiply(10, 5)
# print(multiplication)

# final_number = add(addition, multiplication)
# print(final_number)

# result = add(num2=12, num1=14)

def multiplyByDefaultParameter(num1, num2, num3=3, num4=4):
    result = num1*num2*num3*num4
    print(f'num1 * num2 * num3 * num4 = {result}')
# multiplyByDefaultParameter(1, 2)
# multiplyByDefaultParameter(1, 2, 5, 6)

def args(*numbers):
    result = 1
    for num in numbers:
        result = result * num
    return result
# final_result = args(1, 2, 3, 4)
# print(f'args final result: {final_result}')

def args1(num1, num2, *numbers):
    result = num1*num2
    for num in numbers:
        result = result * num
    return result
# final_result = args(1, 2, 3, 4, 5, 6)
# print(f'args1 final result: {final_result}')

def ful_name(f_name, l_name):
    name = f'{f_name} {l_name}'
    return name
# name = ful_name(l_name='Chowdhury', f_name='Asif')
# print(name)

def long_name(**kargs):
    print(kargs)
# long_name(first='Dr.', last='Chowdhury', middle='Asif')

def long_name1(**kargs):
    for key, value in kargs.items():
        print(key, ': ', value)
# long_name1(first='Dr.', last='Chowdhury', middle='Asif')

def name_mixed(first, last, **name_parts):
    print(first, last, name_parts)
# name_mixed(first='chowdhury', last='choto', middle='majari')

def all_types(first, *args, **kargs):
    print(first)
    print(args)
    print(kargs)
# all_types('Asif', 'Ali', 'Akib', 'Arnab', name='Abdul', father='Latif')
