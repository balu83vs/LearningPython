"""
def times():
    
    def rec(step):
        el = ['1', '2', '3', '4']
        if 4 <= step <= 16:
            line = el[-int(step/4)] * step
            print(line.center(16))
            rec(step-4)
    rec(16)  
    def rec(step):
        el = ['1', '2', '3']
        if 8 <= step <= 16:
            line = el[- int(step/4) + 1] * step
            print(line.center(16))
            rec(step+4)
    rec(8)  

times()  
"""
#
"""
films = {'Spider-Man: No Way Home': {'imdb': 8.8, 'kinopoisk': 8.3},
         'Don"t Look Up': {'imdb': 7.3, 'kinopoisk': 7.6},
         'Encanto': {'imdb': 7.3, 'kinopoisk': 7.4},
         'The Witcher': {'imdb': 8.2, 'kinopoisk': 7.3},
         'Ghostbusters: Afterlife': {'imdb': 7.3, 'kinopoisk': 8},
         'Harry Potter 20th Anniversary: Return to Hogwarts': {'imdb': 8.1, 'kinopoisk': 8.2},
         'Shingeki no Kyojin': {'imdb': 9.0, 'kinopoisk': 8.3},
         'The Matrix': {'imdb': 8.7, 'kinopoisk': 8.5},
         'The Dark Knight': {'imdb': 9.0, 'kinopoisk': 8.5},
         'The Shawshank Redemption': {'imdb': 9.3, 'kinopoisk': 9.1},
         'Avengers: Endgame': {'imdb': 8.4, 'kinopoisk': 7.7}}

print(min(films, key=lambda x: sum(films[x].values())/2))
"""

# Функция non_negative_even()
"""
def non_negative_even(ns): 
    return all([True if (x >= 0 and x%2 == 0) else False for x in ns])

print(non_negative_even([0, 2, 4, 8, 16]))
"""

# Функция is_greater()
"""
def is_greater(list, n):
    return any(map(lambda x: sum(x) > n, list))

data = [[0, 1, 2], [0, 3], [1, 1, 1], [3]]
print(is_greater(data, 3))
"""

# Необычная сортировка
"""
data = 'Sorting1234'

data = [el for el in data]

print(sorted(sorted(data), key = lambda x: (x.islower(), x.isupper(), x.isdigit() and int(x) % 2 > 0), reverse = True))
"""
# АНОТАЦИЯ ТИПОВ
"""
def cyclic_shift(numbers: list[int|float], step: int) -> None:
    for i in range(len(numbers) - step):
        numbers.append(numbers.pop(0))

numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, -2)

print(numbers) 
"""
