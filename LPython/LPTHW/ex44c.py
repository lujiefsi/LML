class Parent(object):
    def altered(self):
        print("PARENTaltered")
class Child(Parent):
    def altered(self):
        print("CHILD,BEFORE PAENT altered")
        super(Child,self).altered()
        print("CHILD,AFTER PARENT altered")
        
dad = Parent()
son = Child()
dad.altered()
son.altered()