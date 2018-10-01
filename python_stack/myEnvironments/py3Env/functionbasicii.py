def countDown(i):
    retarr = [i]
    for j in range(i-1,0,-1):
        retarr.append(j)
    else:
        return retarr

print(countDown(5))

def printFirstReturnSecond(arr):
    print(arr[0])
    return arr[1]

print(printFirstReturnSecond([25,7]))

def firstPlusLength(arr):
    return arr[0]+len(arr)

print(firstPlusLength([11,22,33,44,55,66,77]))

def valuesGreaterThanTheSecond(arr):
    tempVal = arr[1]
    retarr = []
    for i in range(len(arr)):
        if arr[i] > tempVal:
            retarr.append(arr[i])
    else:
        return retarr

print(valuesGreaterThanTheSecond([1,5,3,4,2,9,8,7,6]))

def lengthAndValue(ilength, ivalue):
    retarr = []
    for i in range(ilength):
        retarr.append(ivalue)
    else:
        return retarr

print(lengthAndValue(14,77)) 
