class Robot:
    def SayHello(self,name1,name2):
        self.name1 = name1
        self.name2 = name2
        print("Hello", self.name1 ,self.name2,sep = ":")

        


x = Robot()
x.SayHello("python","Perl")

print("Name :", __name__) 
