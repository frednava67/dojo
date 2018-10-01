# Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big". Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].

def makeItBig(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr.pop(i)
            arr.insert(i,"big")
    else:
        return arr
print("makeItBig")
print(makeItBig([-1,3,5,-5]))

# Count Positives - Given an array of numbers, create a function to replace last value with number of positive values. Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).

def countPositives(arr):
    totPos = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            totPos+=1
    else:
        arr.pop(i)
        arr.insert(i, totPos)
        return arr

print(countPositives([-1,3,5,6,7,8,9,-5]))

# SumTotal - Create a function that takes an array as an argument and returns the sum of all the values in the array.  For example sumTotal([1,2,3,4]) should return 10

def sumTotal(arr):
    totSum = 0
    for i in range(len(arr)):
        totSum += arr[i]
    else:
        return totSum

print(sumTotal([1,2,3,4]))

# Average - Create a function that takes an array as an argument and returns the average of all the values in the array.  For example multiples([1,2,3,4]) should return 2.5

def returnAverage(arr):
    totSum = 0
    for i in range(len(arr)):
        totSum += arr[i]
    else:
        return totSum/len(arr)

print(returnAverage([1,2,3,4]))
    


# Length - Create a function that takes an array as an argument and returns the length of the array.  For example length([1,2,3,4]) should return 4

def returnArrayLength(arr):
    return len(arr)

print("returnArrayLength")
print(returnArrayLength([1,2,3,4]))


# Minimum - Create a function that takes an array as an argument and returns the minimum value in the array.  If the passed array is empty, have the function return false.  For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.

def returnMin(arr):
    if len(arr) == 0:
        return false
    curMin = 0
    for i in range(len(arr)):
        if arr[i] < curMin:
            curMin += arr[i]
    else:
        return curMin

print("returnMin")
print(returnMin([1,2,3,4]))
print(returnMin([-1,-2,-3]))


# Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.  If the passed array is empty, have the function return false.  For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.





# UltimateAnalyze - Create a function that takes an array as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.





# ReverseList - Create a function that takes an array as an argument and return an array in a reversed order.  Do this without creating an empty temporary array.  For example reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.