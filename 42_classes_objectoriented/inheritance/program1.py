

class x:
    def m1(self):
        self.i = 1000

class y(x):
    def m2(self):
        self.j = 2000

y1 = y()
y1.m1()
y1.m2()
print y1.i
print y1.j
