def func_fizz_buzz():
    fizz_buzz_list = []
    for i in range(1, 31):
        default_value = str(i)
        if i % 3 == 0 and i % 5 == 0:
            default_value = 'FizzBuzz'
        elif i % 3 == 0:
            default_value = 'Fizz'
        elif i % 5 == 0:
            default_value = 'Buzz'
        fizz_buzz_list.append(default_value)
    return fizz_buzz_list


print(func_fizz_buzz())
