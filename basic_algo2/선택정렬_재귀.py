def selectionSort(xs):
    if xs != []:
        smallest = min(xs)
        xs.remove(smallest)
        return [smallest] + selectionSort(xs)
    else:
        return []

xs = [6,5,4,3,2,1]

print(selectionSort(xs))

def selectionSoraa(arr):
    if arr != []:
        min_value = min(arr)
        arr.remove(min_value)
        return [min_value] + selectionSoraa(arr)
    else:
        return []