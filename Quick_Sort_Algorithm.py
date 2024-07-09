def quickSort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
        itemsGreater = []
        itemsLower = []
        for item in sequence:
            if item > pivot:
                itemsGreater.append(item)
            else:
                itemsLower.append(item)
        return quickSort(itemsLower) + [pivot] + quickSort(itemsGreater)
print(quickSort([4,3,6,8,1,0,2,2,5,8,9]))