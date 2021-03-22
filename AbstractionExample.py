# This is an example of the OOP concept of Abstraction.

from abc import ABC, abstractmethod
class abstPClass(ABC):
#concrete\normal method
    def display(self, x):
        print("the value you provided is :", x)
    @abstractmethod
    def WhatCls(self):
        print("This abstract method is inside the parent class")

class cCls1(abstPClass):
    def WhatCls(self):
        print("This abstract method is inside the 1st child class")

class cCls2(abstPClass):
    def WhatCls(self):
        print("This abstract method is inside the 2nd child class")

#creating objects
Cls1_obj = cCls1()
Cls1_obj.WhatCls()
Cls1_obj.display(input("Please type an int\n: "))

Cls2_obj = cCls2()
Cls2_obj.WhatCls()
Cls2_obj.display(input("Please type an int\n:"))


# This example is using the Abstact method (WhatCls) inside of different Child classes [cCls1, and cCls2].
# The astract method is initialized inside its parent abstract class (abstPClass). The actual abstract class
# has no instances, because that would prompt an error.


# The advantage of abstract classes and methods is that it allows the programmer to imply a use but not have to
# implement it. Implementation comes in
# when you create another class then then you can add the functionality to it. From my understanding this is similar
# to polymorphism. The difference is that a method used in polymorphism has its own implementation where it's
# first created, whereas abstraction only uses it in its child classes.
# The ability to imply, but not implement allows the user to display a the use of a method with-out showing the ins and outs.

# thanks for reading
