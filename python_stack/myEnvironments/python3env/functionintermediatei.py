# Create beCheerful().  Within it, print string "good morning!" 98 times.
print("*"*98)
def beCheerful(name='', repeat=1):
	print(f"good morning {name}\n"*repeat)
beCheerful()
beCheerful(name="john")
beCheerful(name="michael", repeat=5)
beCheerful(repeat=5, name="kb")
beCheerful(name="aa")
# helpful tips for the next assignment
import random
print(random.random()) # returns a random floating number between 0.000 to 1.000
print(random.random()*50) # returns a float between 0.000 to 50.000
int( 3.654 ) # returns 3
round( 3.654 ) # returns 4

#randInt() returns a random integer between 0 to 100

def randInt1():
    return int(random.random()*100)

print("randInt1()")
print(randInt1())
print(randInt1())
print(randInt1())


#randInt(max=50) returns a random integer between 0 to 50

def randInt2(max=100):
    return int(random.random()*max)

print("randInt2(max=50)")
print(randInt2(max=3))
print(randInt2(max=33))
print(randInt2(max=1000))


#randInt(min=50) returns a random integer between 50 to 100

def randInt3(min=1):
    return int(random.random()*50) + min

print("randInt3(min=50)")
print(randInt3(min=50))

#randInt(min=50, max=500) returns a random integer between 50 and 500

def randInt4(min=50, max=500):
    return int(random.random()*max) + min

print("randInt4(min=50,max=500)")
print(randInt4(min=50,max=500))
print("randInt4(min=5,max=25)")
print(randInt4(min=5,max=25))
print("randInt4(min=1,max=5)")
print(randInt4(min=1,max=5))