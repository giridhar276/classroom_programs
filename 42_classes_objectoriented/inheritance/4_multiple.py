


class x:
    def m1(self):
        print "In method1 of X"


class y(x):
    def m2(self):
        print "In method2 of Y"

class z(x,y):
    def m3(self):
        print "In method3 of Z"



z1 = z()

z1.m1()

z1.m2()

z1.m3()


y1 = y()
y1.m2()


x1 = x()
x1.m1()
