
import sys                           # простые замеры

print(sys.getsizeof(10))
print(sys.getsizeof(True))
print(sys.getsizeof(None))
print(sys.getsizeof(''))
print(sys.getsizeof('beegeek'))

                                     # глубокие замеры   

from pympler import asizeof
obj = [1, 2, (3, 4), 'text']
print(asizeof.asizeof(obj))

print(asizeof.asized(obj, detail=1).format())