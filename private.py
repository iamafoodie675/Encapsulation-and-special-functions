class myClass:
    __privateVar = 27
    
    def __privMeth(self):
        print("i'm inside class myClass")
        
    def hello(self):
        print("private Variable value: ", myClass.__privateVar)
        
ob1 =myClass()
ob1.hello()
ob1.__privMeth()
print(ob1.__privateVar)