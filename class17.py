class Person:
    def say_hi(self):
        self.name="abc"
        print("Hellow,how are you"+ self.name+"?")
p=Person()
p.say_hi()
#
class Person:
    def __init__(self,name):
        self.name=name
    def say_hi(self):
        self.name="abc"
        print("Hellow,how are you"+ self.name+"?")
p=Person("abc")
p.say_hi()