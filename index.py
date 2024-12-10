def quick_sort(arr):
    """
    Implementa o algoritmo Quick Sort.
    :param arr: Lista de números a ser ordenada.
    :return: Lista ordenada.
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    smaller = [x for x in arr[:-1] if x <= pivot]  
    greater = [x for x in arr[:-1] if x > pivot]   

    return quick_sort(smaller) + [pivot] + quick_sort(greater)

if __name__ == "__main__":
    numbers = [8, 3, 1, 7, 0, 10, 2]
    print("Lista original:", numbers)
    sorted_numbers = quick_sort(numbers)
    print("Lista ordenada:", sorted_numbers)
