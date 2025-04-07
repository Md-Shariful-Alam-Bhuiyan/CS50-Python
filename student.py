class Student:
    def __init__(self, name, house, patronus= None):

        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    # getter method in python
    @property
    def name(self):
        return self._name

    # Setter method in python
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name

    # getter method in python
    @property
    def house(self):
        return self._house

    # Setter method in python
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

    @classmethod
    def read(cls):
        print("This is a class method")




    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "🪄"

def main():
    student = Student.get()
    # student.read()
    # student = get_student()
    # print(f"{student.name} from {student.house}")
    print(student)

    # print("Expecto Patronum!")
    # print(student.charm())



# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     # patronus = input("Patronus: ")
#     return Student(name, house)




if __name__ == "__main__":
    main()
