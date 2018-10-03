class Node():
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None

class DList():
    def __init__(self):
        self.head = None

    def printAllValues(self):
        if self.head == None:
            print("======== NOTHING TO PRINT =========")
            return self

        print("===== START Printing All Values going FORWARD ======")
        o = self.head
        while o.next != None:
            print(o.value)
            o = o.next
        print(o.value)
        print("===== END Printing All Values going FORWARD ========")      

        print("===== START Printing All Values going BACKWARD ======")
        while o.prev != None:
            print(o.value)
            o = o.prev
        print(o.value)
        print("===== END Printing All Values going BACKWARD ========")  

        return self

    def addNode(self, val):
        new = Node(val)

        if self.head == None:
            self.head = new
        else:
            old = self.head
            old.prev = new
            new.next = old
            self.head = new
        return self

    def removeNode(self, val):
        new = self.head

        if new.value == val:
            self.head = new.next
            new.next = None
            new.prev = None
            return self

        old = new
        while new.value != val and new.next != None:
            old = new
            new = new.next

        temp = new.next
        old.next = temp
        temp.prev = old
        new.prev = None
        new.next = None
        return self

    def insertNode(self, val, idx):
        new = Node(val)
        old = self.head

        if idx == 0:
            self.head = new
            new.next = old
            old.prev = new
            return self

        counter = 0
        while counter != idx-1 and old.next != None:
            old = old.next
            counter+=1

        temp = old.next
        temp.prev = new
        new.next = temp
        old.next = new
        new.prev = old

        return self        

dL = DList()
dL.addNode("Epsilon")
dL.addNode("Drudge")
dL.addNode(1111)
dL.addNode("Banana")
dL.addNode(12345)
dL.printAllValues()
dL.removeNode(1111)
dL.printAllValues()
dL.addNode("Cherry")
dL.printAllValues()
dL.insertNode("Horse",3)
dL.printAllValues()
dl2 = DList()
dl2.addNode("lonely")
dl2.printAllValues()
dl2.removeNode("lonely")
dl2.printAllValues()
