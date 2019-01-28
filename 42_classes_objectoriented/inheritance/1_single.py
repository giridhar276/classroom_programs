
### single inheritance

class x:
    def m1(self):
        print "In method1 of X"


class y(x):
    def m2(self):
        print "In method2 of Y"


y1 = y()

y1.m1()
y1.m2()

