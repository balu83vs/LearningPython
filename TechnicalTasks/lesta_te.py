from timeit import default_timer
from collections import deque

# декоратор подсчета времени выполнения
def show_time(func): 
    def wraper(*args):
        start_time = default_timer()
        res = func(*args)
        total_time = default_timer() - start_time
        print('Время выполнения:{:.10f}'.format(total_time))
        print('Результат:{}'.format(res))
        return res
    return wraper 


# реализация на базе списка 
class FIFO_list:
    def __init__(self: list) -> None:
        self.elements: list(any) = []
        
    @show_time    
    def get_el(self: list) -> any:
        if self.elements:
            return self.elements.pop(0)
        else: 
            return 'Очередь пуста'
        
    @show_time
    def add_el(self: list, el: any) -> None:
        self.elements.append(el)
        

# реализация на базе списка и итератора     
class FIFO_list_iter:
    def __init__(self: list) -> None:
        self.elements: list(any) = []
      
    def __iter__(self):
        return self
    
    @show_time
    def __next__(self):
        try:
            res = self.elements[0]
            del self.elements[0]
            return res
        except IndexError:
            print('Очередь пуста')
            raise StopIteration

    @show_time
    def add_el(self: list, el: any) -> None:
        self.elements.append(el)


# реализация на базе deque
class FIFO_deque:
    def __init__(self):
        self.elements = deque()
    
    @show_time    
    def get_el(self):
        if self.elements:
            return self.elements.popleft()    
        else:
            return 'Очередь пуста'

    @show_time
    def add_el(self, element):
        self.elements.append(element)       
        

# точка входа        
if __name__ == '__main__':
    test1 = FIFO_list()
    test2 = FIFO_list_iter()
    test3 = FIFO_deque()
    
    print('FIFO на базе простого списка')
    print('_' * 30)
    test1.add_el(1)
    test1.get_el()
    print('_' * 30)
    print('FIFO на базе простого списка с итератором')
    print('_' * 30)
    test2.add_el(1)
    for el in test2:
        print(el)
    print('_' * 30)
    print('FIFO на базе deque')
    print('_' * 30)
    test3.add_el(1)
    test3.get_el()
    print('_' * 30)