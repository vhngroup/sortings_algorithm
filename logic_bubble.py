#Logic part or algoritm
def sorting_burbble(arr):
    n = len(arr)
    for i in range(n):
        for  j in range(0, n-i-1):
            if arr[j] > arr[ j + 1]:
                arr[j], arr[j + 1] = arr[ j + 1] , arr[j]

lista = [10, 1, 12, 9, 89]

sorting_burbble(lista)
print(lista)
