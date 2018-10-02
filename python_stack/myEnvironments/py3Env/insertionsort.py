def insertion_sort(arr):
    arrLen = len(arr)
    for curPointerLoc in range(1,arrLen):
        for innerLoop in range(curPointerLoc-1,-1,-1):
            print(curPointerLoc,arr[curPointerLoc], innerLoop, arr[innerLoop])
    else:
        return "done"

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("original array: ", [5,6,3,9,2,8])
print(insertion_sort([5,6,3,9,2,8]))
# print("original array: ", [1,2,3,4,5,6])
# print(insertion_sort([1,2,3,4,5,6]))
# print("original array: ", [19,17,14,12,11,6])
# print(insertion_sort([19,17,14,12,11,6]))
# print("original array: ", [19,17])
# print(insertion_sort([19,17]))
