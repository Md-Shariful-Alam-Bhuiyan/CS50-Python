class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError
        self.name = name

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def __str__(self):
        return f"Professor {self.name} works on {self.subject}"




def main():
    wizard = Wizard("Harry")
    print(wizard.name)
    student = Student("James", "Gryffindor")
    print(student)
    professor = Professor("David Malan", "Computer Science")
    print(professor)

if __name__ == "__main__":
    main()
