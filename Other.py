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

# Распределение по комнатам

import random

    #Реализовать класс Room()
class Room:

    room_number = 0

    #У него должно быть поле users типа список []
    def __init__(self):
        self.users = []
        Room.room_number +=1
        self.room_number = Room.room_number
                
    #Реализовать у Класса метод append_user_id он принимает user_id и добавляет его в users    
    def append_user_id(self, user_id):
        self.users.append(user_id)    

if __name__ == "__main__":
    #создать 3 переменные с экземпляром класса Room
    one = Room() 
    two = Room()  
    three = Room() 

    id_list = [100, random.randint(1,99), random.randint(1,99)]
    random.shuffle(id_list)

    #у каждой переменной вызвать метод append_user_id и передать туда рандомной число но у одной из 3 user_id должен  быть 100
    one.append_user_id(id_list[0])
    two.append_user_id(id_list[1])
    three.append_user_id(id_list[2])
    
    rooms = [one, two, three]

	#Пример:
	#room1 = создаем экземпляр класса
	#Дале помещаем эти переменные в новый список rooms

	#Задача найти комнату в которой находится вот такой 100 user_id
    for room in rooms:
        if 100 in room.users:
            print(f'User с id 100 находится в комнате {room.room_number}')


    

	
        

