

class Y:
    def m1(self,*args):
        for p in args:
            print p


y1 =Y()

y1.m1(10,20)

y1.m1(100,200,300)

y1.m1("perl","unix","java")
