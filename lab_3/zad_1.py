# zad_1
class Student:
    def __init__(self, name, marks):
        self._name = name
        self._marks = marks

    @property
    def name(self) -> str:
        return self._name

    @property
    def marks(self) -> list:
        return self._marks

    def is_passed(self):
        return (sum(self._marks)/len(self._marks)) > 50

stud1 = Student("Marian", [50,51,60])
stud2 = Student("Iwona", [10,10,5,7])

print(stud1.is_passed())
print(stud2.is_passed())