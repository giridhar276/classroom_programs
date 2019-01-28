class Robot:
    ''' document string example '''
 
    def SayHello(self,name):
        
        self.name =  name    # local variable
        print("Hello " + self.name)
        

# creating object to a class
# Object initialization 
x = Robot()
y= Robot()
z = Robot()


x.SayHello("Perl" ) # Hello Perl
y.SayHello("Python")# Hello Python
z.SayHello("Ruby")  # Hello Ruby
print("You are executing this module directly")

 
