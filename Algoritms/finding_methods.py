                                                 # бинарный поиск
"""
Учитывая отсортированный массив n целые числа и целевое значение, определите, существует ли цель в массиве в 
логарифмическом масштабе, используя алгоритм двоичного поиска. Если цель существует в массиве, выведите ее индекс.
"""

# (итеративная реализация)
"""
def bin_find(input_data, find):
    start = 0
    end = len(input_data) - 1

    while start <= end:
        middle = (end + start) // 2
        if find == input_data[middle]:
            return middle
        elif find < input_data[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return -1

if __name__ == '__main__':
    input_data = [1,4,6,9,0,7,3,2]
    input_data.sort()
    find = 9
    res = bin_find(input_data, find)
    print('Ваш ответ:', res)
"""

#(рекурсивный) 
"""   
def bin_find(input_data, start, end, find):

    if start > end:
        return -1
    
    mid = (start + end) // 2

    if find == input_data[mid]:
        return mid
    elif find < input_data[mid]:
        return bin_find(input_data, start, mid-1, find)
    else:
        return bin_find(input_data, mid+1, end, find)
    
if __name__ == '__main__':
    input_data = [1,4,6,9,0,7,3,2]
    input_data.sort()
    find = 9
    start = 0
    end = len(input_data) - 1
    res = bin_find(input_data, start, end, find)
    print('Ваш ответ:', res)
"""


                                               # Поиск в ширину (BFS)
"""
алгоритм обхода или поиска древовидных или графовых структур данных. Он начинается с корня дерева (или некоторого произвольного 
узла Graph, иногда называемого 'ключом поиска') и сначала исследует соседние узлы, прежде чем перейти к соседям следующего уровня.
"""

# (итеративная реализация)
"""
from collections import deque
 
# Класс для представления graphического объекта
class Graph:
    # 1ТП4Т Конструктор
    def __init__(self, edges, n):
 
        # Список списков для представления списка смежности
        self.adjList = [[] for _ in range(n)]
 
        # добавляет ребра в неориентированный graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)   
 
 
# Выполнить BFS на Graph, начиная с вершины `v`
def BFS(graph, v, discovered):
 
    # создать queue для выполнения BFS
    q = deque()
 
    # пометить исходную вершину как обнаруженную
    discovered[v] = True
 
    # ставит в queue исходную вершину
    q.append(v)
 
    # Цикл # до тех пор, пока queue не станет пустой
    while q:
 
        # удалить передний узел из очереди и распечатать его
        v = q.popleft()
        print(v, end=' ')
 
        # делаем для каждого ребра (v, u)
        for u in graph.adjList[v]:
            if not discovered[u]:
                # пометить его как обнаруженный и поставить в queue
                discovered[u] = True
                q.append(u)
 
if __name__ == '__main__':
    # Список ребер Graph согласно приведенной выше схеме
    edges = [
        (1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9),
        (5, 10), (4, 7), (4, 8), (7, 11), (7, 12)
        # вершины 0, 13 и 14 являются одиночными узлами
    ]
 
    # общее количество узлов в Graph (от 0 до 14)
    n = 15
 
    # строит graph по заданным ребрам
    graph = Graph(edges, n)
 
    # для отслеживания обнаружена вершина или нет
    discovered = [False] * n
 
    # Выполнить обход BFS от всех необнаруженных узлов к
    # охватывает все связанные компоненты Graph
    for i in range(n):
        if not discovered[i]:
            # начать обход BFS из вершины i
            BFS(graph, i, discovered)
"""            