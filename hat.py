import random

# class Hat:

#     def __init__(self):
#         self.houses = ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]

#     def sort(self,name):
#         print(name, " is in ", random.choice(self.houses))

#=====================================================================================#

class Hat:
    # class variable
    houses = ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]

    # class method
    @classmethod
    def sort(cls,name):
        print(name, " is in ", random.choice(cls.houses))


# hat = Hat()
# hat.sort("Harry")

Hat.sort("harry")
