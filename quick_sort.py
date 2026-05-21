def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range (low, high):
        if array[j] <= pivot:
            i += 1
        array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return i+1
def quickSort(array, low=1, high = None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quickSort(array, low, pivot_index-1)
        quickSort(array, pivot_index+1, high)
mylist = [64, 34, 25, 5, 22, 11, 90, 12]
quickSort(mylist)
print(mylist)