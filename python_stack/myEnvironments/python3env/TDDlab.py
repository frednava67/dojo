# import the python testing frameworkcopy
import unittest
# our "unit"
# this is what we are running our test on

def reverseList(arr=None):
    if arr == None or type(arr) is not list:
        return None
    for i in range(0,int(len(arr)/2)):
        temp = arr[i]
        arr[i] = arr[len(arr)-1-i]
        arr[len(arr)-1-i] = temp
    else:
        return arr

def isPalindrome(s=None):
    if s == None or s =="" or type(s) is not str:
        return False
    for i in range(0,int(len(s)/2)):
        if s[i] != s[len(s)-1-i]:
            return False
    else:
        return True

denominations = [{  "name": "Quarters",
                    "value": 25},
                {   "name": "Dimes",
                    "value": 10},   
                {   "name": "Nickels",
                    "value": 5},
                {   "name": "Pennies",
                    "value": 1}
                ]

def coins(i=None):
    if i == None or type(i) is not int:
        return None
    retarr = []
    curVal = i
    curCount = 0
    for d in denominations:
        while curVal >= d["value"]:
            curCount+=1
            curVal-=d["value"]
        retarr.append(curCount)
        curCount = 0
    else:
        return retarr

def Factorial(i=None):
    if i == None or type(i) is not int or i < 0:
        return None
    elif i == 0 or i == 1:
        return 1
    else:
        return i * Factorial(i-1)

def Fib(i=None):
    if i == None or type(i) is not int or i < 0:
        return None
    elif i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return i + Fib(i-1)



class reverseListTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(reverseList([1,3,5]), [5,3,1])
    def test2(self):
        return self.assertEqual(reverseList([2,4,-3]), [-3,4,2])
    def test3(self):
        return self.assertEqual(reverseList([2]), [2])
    def test4(self):
        return self.assertEqual(reverseList(), None)
    def test5(self):
        return self.assertIsNone(reverseList())        
    def test6(self):
        return self.assertEqual(reverseList("STRING"), None)
    def test7(self):
        return self.assertIsNone(reverseList("STRING"))        
    def test8(self):
        return self.assertEqual(reverseList([1,1,1,1,1,1,1,1,1]), [1,1,1,1,1,1,1,1,1])        
    def test9(self):
        return self.assertNotEqual(reverseList([1,3,5]), [1,3,5])    

class isPalindromeTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(isPalindrome("racecar"), True)
    def test2(self):
        return self.assertEqual(isPalindrome("rabbit"), False)
    def test3(self):
        return self.assertFalse(isPalindrome())
    def test4(self):
        return self.assertFalse(isPalindrome(5))        
    def test5(self):
        return self.assertEqual(isPalindrome("r"), True)
    def test6(self):
        return self.assertEqual(isPalindrome("rrrrr"), True) # odd number characters
    def test7(self):
        return self.assertEqual(isPalindrome("rrrrrr"), True) # even number characters
    def test8(self):
        return self.assertEqual(isPalindrome(""), False)

class coinsTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(coins(87), [3,1,0,2])
    def test2(self):
        return self.assertEqual(coins(92), [3,1,1,2])
    def test3(self):
        return self.assertEqual(coins(0), [0,0,0,0])        
    def test4(self):
        return self.assertEqual(coins(), None)
    def test5(self):
        return self.assertEqual(coins("a"), None)
    def test6(self):
        return self.assertEqual(coins(1), [0,0,0,1])
    def test7(self):
        return self.assertEqual(coins(5), [0,0,1,0])
    def test8(self):
        return self.assertEqual(coins(10), [0,1,0,0])
    def test9(self):
        return self.assertEqual(coins(25), [1,0,0,0])

class FactorialTest(unittest.TestCase):
    def test1(self):
        return self.assertIsNone(Factorial())
    def test2(self):
        return self.assertIsNone(Factorial("a"))
    def test3(self):
        return self.assertEqual(Factorial(0), 1)
    def test4(self):
        return self.assertEqual(Factorial(1), 1)
    def test5(self):
        return self.assertEqual(Factorial(5), 120)
    def test6(self):
        return self.assertIsNone(Factorial(-10))

class FibTest(unittest.TestCase):
    def test1(self):
        return self.assertIsNone(Fib())
    def test2(self):
        return self.assertIsNone(Fib("a"))
    def test3(self):
        return self.assertIsNone(Fib(-10))
    def test4(self):
        return self.assertEqual(Fib(0), 0)
    def test5(self):
        return self.assertEqual(Fib(1), 1)
    def test6(self):
        return self.assertEqual(Fib(10), 55)

if __name__ == "__main__":
    unittest.main()
