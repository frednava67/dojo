x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#How would you change the value 10 in x to 15?  Once you're done x should then be [ [5,2,3], [15,8,9] ].  

def changeval1(thing):
    thing[1][0] = 15

#print(x)
#changeval1(x)
#print(x)

#How would you change the last_name of the first student from 'Jordan' to "Bryant"?

def changeval2(thing):
    thing[0]["last_name"] = "Bryant"

#print(students)
#changeval2(students)
#print(students)

#For the sports_directory, how would you change 'Messi' to 'Andres'?

def changeval3(thing):
    thing["soccer"][0] = "Andres"

#print(sports_directory)
#changeval3(sports_directory)
#print(sports_directory)

#For z, how would you change the value 20 to 30?

def changeval4(thing):
    thing[0]["y"] = 30

#print(z)
#changeval4(z)
#print(z)

#2. Create a function that given a list of dictionaries, it loops through each dictionary in the list and prints each key and the associated value.  For example, given the following list:

students1 = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(thing):
    for i in students1:
        print("first_name - " + i["first_name"] + ", " + "last_name - " + i["last_name"]) 

#iterateDictionary(students1)

#3. Create a function that given a list of dictionaries and a key name, it outputs the value stored in that key for each dictionary.  For example, iterateDictionary2('first_name', students) should output

def iterateDictionary2(key, thing):
    for i in students1:
        print(i[key]) 

iterateDictionary2("first_name", students1)

#4. Say that

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

#Create a function that prints the name of each location and also how many locations the Dojo currently has.  Have the function also print the name of each instructor and how many instructors the Dojo currently has.  For example, printDojoInfo(dojo) should output

#7 LOCATIONS
#San Jose
#Seattle
#Dallas
#Chicago
#Tulsa
#DC
#Burbank
#    
#8 INSTRUCTORS
#Michael
#Amy
#Eduardo
#Josh
#Graham
#Patrick
#Minh
#Devon

def printDojoInfo(thing):
    print(str(len(thing["locations"])) + " LOCATIONS")
    for l in thing["locations"]:
        print(l)

    print("")

    print(str(len(thing["instructors"])) + " INSTRUCTORS")
    for i in thing["instructors"]:
        print(i)
    
printDojoInfo(dojo)

