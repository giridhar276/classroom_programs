




class x:
    def m1(self):
        print "In method1 of X"


class y(x):
    def m2(self):
        print "In method2 of Y"

class z(x):
    def m3(self):
        print "In method3 of Z"



y1 = y()

y1.m1()

y1.m2()

z1 = z()
z1.m1()

z1.m3()
