# This is an example of Polymorphic methods
# Our base class (gymMember) sets our base attributes, and a method
# to its corresponding child classes
# the method accessAuth will be used in different classes to check
# if the gym member will be able to access area




#Parent class
class gymMember:
        MemberName = ""
        MemberId = ""
        AccessPin = 0
        Memberlevel = 0
    

        def accessAuth(self):
            MemberName = input("Please enter your name!\n:")
            MemberId = input("What is your member Id?\n: ")
            AccessPin = input("What is your Access Pin?\n: ")
            Memberlevel = input ("What is your member level\n: ")
        
            if Memberlevel == 0:
                print("Hello {}, you have access to this area because you are a level {} member!".format(MemberName, Memberlevel))
            else:
                 print("Hmmm, you do not have access to the area, if this is an error please contact front desk!")


#child to (gymMember)
class Level_1Member(gymMember):

#the accessAuth() method now checks if member level one
    def accessAuth(self):
        MemberName = input("Please enter your name!\n:")
        MemberId = input("What is your member Id?\n: ")
        AccessPin = input("What is your Access Pin?\n: ")
        Memberlevel = input("Hi {}, what is your member level\n:".format(MemberName))    
        
        if int(Memberlevel) == 1:
            print("Hello {}, you have access to this area because you are a level {} member!".format(MemberName, Memberlevel))
        else:
             print("Hmmm, you do not have access to the area, if this is an error please contact front desk!")
    



#child to (gymMember)
class Level_2Member(gymMember):

#the accessAuth() method now checks if member level two 
    def accessAuth(self):
        MemberName = input("Please enter your name!\n:")
        MemberId = input("What is your member Id?\n: ")
        AccessPin = input("What is your Access Pin?\n: ")
        Memberlevel = input("Hi {}, what is your member level\n:".format(MemberName))    
        
        if int(Memberlevel) == 2:
            print("Hello {}, you have access to this area because you are a level {} member!".format(MemberName, Memberlevel))
        else:
             print("Hmmm, you do not have access to the area, if this is an error please contact front desk!")




    


Lev_1 = Level_1Member()
Lev_1.accessAuth()

    
Lev_2 = Level_2Member()
Lev_2.accessAuth()



    
