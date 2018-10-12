# _.map([1,2,3], lambda x: x*2) # should return [2,4,6]
# _.find([1,2,3,4,5,6], lambda x: x>4) # should return the first value that is greater than 4
# _.filter([1,2,3,4,5,6], lambda x: x%2==0) # should return [2,4,6]
# _.reject([1,2,3,4,5,6], lambda x: x%2==0) # should return [1,3,5]

class Underscore:
    def map(self, arr, callback):
        for i in range(len(arr)):
            arr[i] = callback(arr[i])
        return arr
            
    def find(self, arr, callback):
        for i in range(len(arr)):
            if callback(arr[i]):
                return arr[i]
        else:
            return None

    def filter(self, arr, callback):
        newarr = []
        for i in range(len(arr)):
            if callback(arr[i]):
                newarr.append(arr[i])
        return newarr

    def reject(self, arr, callback):
        newarr = []
        for i in range(len(arr)):
            if callback(arr[i]) == False:
                newarr.append(arr[i])
        return newarr

# you just created a library with 5 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
mapcall = _.map([1,2,3], lambda x: x*2)
print(mapcall)
findcall = _.find([1,2,3,4,5,6], lambda x: x>4)
print(findcall)
filtercall = _.filter([1, 2, 3, 4, 5, 6], lambda x: x%2==0)
print(filtercall)
rejectcall = _.reject([1,2,3,4,5,6], lambda x: x%2==0)
print(rejectcall)

# should return [2, 4, 6] after you finish implementing the code above
