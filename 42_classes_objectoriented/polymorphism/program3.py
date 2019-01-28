

## method overriding

'''
the concept of defining multiple methods with the samse name with the no. of paramters

One is superclass and another is subclass is known as method overriding

'''



class parent:
    def myMethod(self):
        print"Calling parent method"

class child(parent):
    def myMethod(self):
        print "calling child method"


c= child()
c.myMethod()

p = parent()

p.myMethod()
