def printState(cpl, cpval, cml, cmval):
    print("CurPointerLoc = ", cpl)
    print("CurPointerLoc Value = ", cpval)
    print("CurMinLoc = ", cml)
    print("CurMinLoc Value = ", cmval)

def selection_sort(arr):
    print(arr)
    print()
    arrLen = len(arr)
    curMinLoc = 0
    for curPointerLoc in range(0,arrLen-1):
        curMinLoc = curPointerLoc
        printState(curPointerLoc, arr[curPointerLoc], curMinLoc, arr[curMinLoc])
        for innerLoop in range(curPointerLoc+1,arrLen):
            print("outerLoop", curPointerLoc)
            print("innerLoop", innerLoop)
            print("===== performing comparison ========")  #need to figure out how to not nuke curMinLoc the next time we find a value smaller than curPointerLoc
            if arr[innerLoop] < arr[curMinLoc]:
                curMinLoc = innerLoop
                print("Found a smaller value")
                printState(curPointerLoc, arr[curPointerLoc], curMinLoc, arr[curMinLoc])
            else:
                print("Didn't find a smaller value")
                printState(curPointerLoc, arr[curPointerLoc], curMinLoc, arr[curMinLoc])
        else:
            if curPointerLoc != curMinLoc:
                print("[[[[[[[ performing swap ]]]]]]]]]]")
                printState(curPointerLoc, arr[curPointerLoc], curMinLoc, arr[curMinLoc])
                temp = arr[curPointerLoc]
                arr[curPointerLoc] = arr[curMinLoc]
                arr[curMinLoc] = temp
            print(arr)
    else:
        return arr

print(selection_sort([5,6,3,9,2,8]))
print(selection_sort([1,2,3,4,5,6]))
print(selection_sort([19,17,14,12,11,6]))