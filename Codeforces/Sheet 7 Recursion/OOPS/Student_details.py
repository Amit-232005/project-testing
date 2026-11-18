# class Student:
#     def input(self):
#         self.name=input()
#         self.rollNo=int(input())
#         self.marks=int(input())
    
#     def display(self):
#         print("Name:",self.name)
#         print("Roll No:",self.rollNo)
#         print("Marks:",self.marks)
#         print("Status:","Passed" if self.is_passed(self.marks) else "Failed")
#         print("-" * 30)
    
#     def is_passed(self,marks):
#         return marks>=40

# s1=Student()
# s1.input()
# s1.display()
    

class Student:
    name = ""
    rollNo = 0
    marks = 0

    def input(self):
        Student.name = input()
        Student.rollNo = int(input())
        Student.marks = int(input())

    def display(self):
        print("Name:", Student.name)
        print("Roll No:", Student.rollNo)
        print("Marks:", Student.marks)
        print("Status:", "Passed" if Student.is_passed() else "Failed")
        print("-"*30)

    @classmethod
    def is_passed(cls):
        return Student.marks >= 40


s1=Student()
s2=Student()

s1.input()
s2.input()

s1.display()
s2.display()