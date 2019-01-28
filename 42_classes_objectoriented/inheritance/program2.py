

class x:
    def m1(self):
        self.i = 1000

class y(x):
    def m2(self):
        self.j = 2000

    def display(self):
        print self.i
        print self.j

y1 = y()
y1.m1()
y1.m2()
y1.display()	
