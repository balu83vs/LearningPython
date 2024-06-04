################################### Алгоритмы сортировок #########################################


# Сортировка вставками (Insertion Sort)
def insert_sorting(unsorting):
    """
    алгоритм сортировки, на каждом шаге которого массив постепенно перебирается слева направо. 
    При этом каждый последующий элемент размещается так, чтобы он оказался между ближайшими 
    элементами с минимальным и максимальным значением.
    """

    for i in range(1, len(unsorting)):
        j = i
        temp = unsorting[i]
        while j > 0 and unsorting[j-1] > temp:
            unsorting[j] = unsorting[j-1]
            j -= 1 
        unsorting[j] = temp

    return unsorting 



# Сортировка выбором (Selection Sort)
def select_sorting(unsorted):
    """
    В алгоритме на каждом шаге выбирается наименьший элемент из оставшихся и меняется местами 
    с элементом, стоящим на текущей позиции. Процесс повторяется до тех пор, пока весь список 
    не будет отсортирован.

    """
    for i in range(0, len(unsorted) - 1):
        smallest = i
        for j in range(i+1, len(unsorted)):
            if unsorted[j] < unsorted[smallest]:
                smallest = j
        unsorted[i], unsorted[smallest] = unsorted[smallest], unsorted[i]      

    return unsorted      



# Быстрая сортировка (Quick Sort)
def quick_sorting(unsorted, start, end):
    """
    Алгоритм использует стратегию «разделяй и властвуй». Он выбирает опорный элемент, разделяет 
    список на две подгруппы — элементы, меньшие опорного, и элементы, большие опорного, затем 
    рекурсивно сортирует каждую из подгрупп.
    """
    if end - start > 1:
        p = partition(unsorted, start, end)
        quick_sorting(unsorted, start, p)
        quick_sorting(unsorted, p+1, end)


def partition(unsorted, start, end):
    pivot = unsorted[start]
    i = start + 1
    j = end - 1

    while True:
        while i <= j and unsorted[i] <= pivot:
            i = i + 1
        while i <= j and unsorted[j] >= pivot:
            j = j - 1

        if i <= j:
            unsorted[i], unsorted[j] = unsorted[j], unsorted[i]
        else:
            unsorted[start], unsorted[j] = unsorted[j], unsorted[start]
    
            return j            



# Сортировка слиянием (Merge Sort)
def merge_sorting(unsorted, start, end):
    """
    алгоритм использует стратегию «разделяй и властвуй». Он разделяет список на две равные части, 
    рекурсивно сортирует каждую из них, а затем объединяет две отсортированные подгруппы в одну 
    упорядоченную последовательность.
    """
    if end - start > 1: 
        mid = (start + end) // 2                     # найти среднюю точку
 
        merge_sorting(unsorted, start, mid)         # разделить/объединить левую половину
        merge_sorting(unsorted, mid, end)           # разделить/объединить правую половину
    
        merge(unsorted, start, mid, end)            # объединяет две половины пробега


def merge(unsorted, start, mid, end):
    left = unsorted[start:mid]
    right = unsorted[mid:end]
    k = start
    i = 0
    j = 0
    
    while start + i < mid and mid + j < end:
        if left[i] <= right[j]:
            unsorted[k] = left[i]
            i = i + 1
        else:
            unsorted[k] = right[j] 
            j = j + 1
        k = k + 1

    if start + i < mid:
        while k < end:
            unsorted[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            unsorted[k] = right[j   ]
            j = j + 1
            k = k + 1               



# Функция для проверки, отсортирован ли `A` в порядке возрастания или нет
def isSorted(A):
 
    prev = A[0]
    for i in range(1, len(A)):
        if prev > A[i]:
            print("MergeSort Fails!!")
            return False
 
        prev = A[i]
 
    return True
 
 

# Реализация алгоритмов сортировок
if __name__ == '__main__':
    A = [12, 3, 18, 24, 0, 5, -2]       # не отсортированная последовательность

    #insert_sorting(A)                  # сортировка вставками
    #select_sorting(A)                  # сортировка выбором
    #quick_sorting(A, 0, len(A))        # быстрая сортировка
    merge_sorting(A, 0, len(A))         # сортировка слиянием


    if isSorted(A):                     # если последовательность отсоритрована
        print(A)                        # выводим