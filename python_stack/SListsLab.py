class Node():
    def __init__(self, val):
        self.value = val
        self.next = None

class SList():
    def __init__(self):
        self.head = None

    def addNode(self,val):
        new = Node(val)
        new.next = self.head
        self.head = new
        return self
    
    def printAllValues(self):
        if self.head == None:
            print("======== NOTHING TO PRINT =========")
            return self

        print("===== START Printing All Values ======")
        o = self.head
        while o.next != None:
            print(o.value)
            o = o.next
        print(o.value)
        print("===== END Printing All Values ========")        
        return self

    def removeNode(self, val):
        new = self.head

        if new.value == val:
            self.head = new.next
            new.next = None
            return self

        old = new
        while new.value != val and new.next != None:
            old = new
            new = new.next

        old.next = new.next
        new.next = None
        return self

    def insertNode(self, val, idx):
        new = Node(val)
        old = self.head

        if idx == 0:
            self.head = new
            new.next = old
            return self

        counter = 0
        while counter != idx-1 and old.next != None:
            old = old.next
            counter+=1

        new.next = old.next
        old.next = new
        return self        


sL = SList()
sL.addNode("Epsilon")
sL.addNode("Drudge")
sL.addNode(1111)
sL.addNode("Banana")
sL.addNode(12345)
sL.printAllValues()
sL.removeNode(1111).removeNode("Epsilon")
sL.printAllValues()
sL.addNode("Epsilon")
sL.addNode("Zebra")
sL.printAllValues()
sL.removeNode("Zebra")
sL.printAllValues()
sL.removeNode("Drudge")
sL.printAllValues()
sL.insertNode("Giraffe",0)
sL.insertNode("Doberman",0)
sL.printAllValues()
sL.insertNode("Horse",3)
sL.printAllValues()
sL.insertNode("Yorkie",6)
sL.printAllValues()
sl2 = SList()
sl2.addNode("lonely")
sl2.printAllValues()
sl2.removeNode("lonely")
sl2.printAllValues()