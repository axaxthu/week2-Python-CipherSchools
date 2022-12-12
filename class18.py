class A:
    def __init__(self) :
        print(self)
        print("intialized")
    def __call__(self) :
        print(self)
        print("I'm dying")

        
#print(a=A())