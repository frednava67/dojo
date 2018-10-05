def selection_sort(arr):
    arrLen = len(arr)
    curMinLoc = 0
    for curPointerLoc in range(0,arrLen-1):
        curMinLoc = curPointerLoc
        for innerLoop in range(curPointerLoc+1,arrLen):
            if arr[innerLoop] < arr[curMinLoc]:
                curMinLoc = innerLoop
        else:
            if curPointerLoc != curMinLoc:
                temp = arr[curPointerLoc]
                arr[curPointerLoc] = arr[curMinLoc]
                arr[curMinLoc] = temp
    else:
        return arr

print("original array: ", [5,6,3,9,2,8])
print(selection_sort([5,6,3,9,2,8]))
print("original array: ", [1,2,3,4,5,6])
print(selection_sort([1,2,3,4,5,6]))
print("original array: ", [19,17,14,12,11,6])
print(selection_sort([19,17,14,12,11,6]))
print("original array: ", [19,17])
print(selection_sort([19,17]))
