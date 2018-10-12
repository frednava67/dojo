class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, arg1, *argv):
        self.result += arg1
        for arg in argv:
            self.result += arg
        return self

    def subtract(self, arg1, *argv):
        self.result -= arg1
        for arg in argv:
            self.result -= arg
        return self


md = MathDojo()
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)