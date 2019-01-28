




class parent:
    def altered(self):
        print "parent altered"


class child(parent):
    def altered(self):
        print "Child before parent altered"


    super(child,self).altered()

    print "Child after parent altered"


dad = parent()

son = child()

dad.altered()

son.altered()
