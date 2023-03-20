"""
import os

clear = lambda: os.system('cls')
exit = 'y'
clear()
while exit not in 'n':
    print('Введите первое число:')
    a = int(input())
    print('Введите второе число:')
    b = int(input())
    print('Введите операцию:')
    ex = input()

    if ex == '+':
        print(f'Результат: {a} {ex} {b} = {a+b}') 
    elif ex == '-':
        print(f'Результат: {a} {ex} {b} = {a-b}') 
    elif ex == '*':
        print(f'Результат: {a} {ex} {b} = {a*b}') 
    elif ex == '/':
        print(f'Результат: {a} {ex} {b} = {a/b}')  
    print()    
    print('Новое вычисление? y/n')
    exit = input()
    clear()
"""

# Правильный пароль
"""
class LoginError(Exception):
    pass

def verification(login, password, success, failure):
    
    password = ''.join(list(filter(lambda x: x if (ord(x) in [el for el in range(ord('A'), ord('z') + 1)]) or x in '1234567890' else None, password)))
    
    try:
        if password.isdigit():
            raise LoginError('в пароле нет ни одной буквы')
        elif password == password.lower():
            raise LoginError('в пароле нет ни одной заглавной буквы')
        elif password == password.upper():
            raise LoginError('в пароле нет ни одной строчной буквы')
        elif password.isalpha():
            raise LoginError('в пароле нет ни одной цифры')
            
    
    except LoginError as er:
        failure(login, er)

    else:
        success(login)

def success(login):
    print(f'Здравствуйте, {login}!')

def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')

verification('Ruslan_Chaniev', 'stepikstepik2', success, failure)    
"""