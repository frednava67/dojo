def selection_sort(arr):
    print(arr)
    arrLen = len(arr)
    for curPointerLoc in range(0,arrLen):
        for innerLoop in range(curPointerLoc+1,arrLen):
            curMinLoc = curPointerLoc
            print(innerLoop, arr)
            if arr[innerLoop] < arr[curPointerLoc]:
                curMinLoc = innerLoop
        else:
            if curPointerLoc != curMinLoc:
                temp = arr[curPointerLoc]
                arr[curPointerLoc] = arr[curMinLoc]
                arr[curMinLoc] = temp

    else:
        return arr

print(selection_sort([5,6,3,9,2,8]))