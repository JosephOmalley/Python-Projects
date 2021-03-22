# this is an example of encapsulation.
# it has an instance of a protected variable
# and a private varible.

#The class "box" will have 2 attributes, Red and yellow balls.
#this box is going to be shipped and is expected to contain The correct number
#of balls. I will make sure of this by setting the varibles as protected vars is a '_' as a prefix

class box:
    def __init__(self):
        self._RedBalls = 5
        self._YellowBalls = 7
    def getTot(self):
        __TotBalls = self._YellowBalls + self._RedBalls 
        print(__TotBalls)
# The Totballs is set as a private var so it's harder to be changed. When a var has a '__' it means it 
# should not be used outside of a class.
obj = box()
obj.getTot()


