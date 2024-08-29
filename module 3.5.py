def summa(n):
    if n == 0:
        return 0
    else:
        return n + summa(n - 1)

print(summa(5))

stack = []
stack.append(1)
print("Добавить элемент" , stack)
stack.append(2)
print("Добавить элемент" , stack)
stack.append(3)
print("Добавить элемент" , stack)
print(stack)
stack.pop()
print('Убрали элемент' , stack)
stack.pop()
print('Убрали элемент' , stack)
stack.pop()
print('Убрали элемент' , stack)


# домашняя работа

def get_multiplied_digits (numbers):
    str_number = str(numbers)
    if len(str_number) > 1:
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return int(str_number)


result = get_multiplied_digits(40203)
print(result)
