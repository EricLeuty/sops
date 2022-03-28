import os
import pickle
from pathlib import Path

#Holds a unique set of students codes in a dictionary
class StudentSet(object):
    def __init__(self, name, students_arg=None):
        self.name = name
        if students_arg is not None:
            self.students = students_arg
        else:
            self.students = {}


    def add_student(self, student):
        try:
            self.students.update({hash(student): student})
        except:
            print("Error: failed to add code to code set.")


    def remove_student(self, id_number):
        try:
            self.students.pop(hash(id_number))
        except:
            print("Error: failed to delete code.")


    def save(self):
        studentset_path = Path(os.getcwd()).parent / "Studentsets" / self.name
        f = open(studentset_path, "w")
        try:
            f = open(studentset_path, "wb")
            pickle.dump(self, f)
            f.close()
        except:
            print("Error: file not found.")


    def load(studentset_name):
        studentset_path = Path(os.getcwd()).parent / "Studentsets" / studentset_name
        try:
            f = open(studentset_path, "rb")
            studentset = pickle.load(f)
            f.close()
            return studentset
        except FileNotFoundError:
            print("Error: file not found.")

    def load_from_path(studentset_path):
        try:
            f = open(studentset_path, "rb")
            studentset = pickle.load(f)
            f.close()
            return studentset
        except FileNotFoundError:
            print("Error: file not found.")


    def print(self):
        for key, value in self.students.items():
            print(key, ' : ', value.to_str())


class Student(object):
    def __init__(self, student_number, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.student_number = student_number
        self.id_number = hash(self)

    def to_str(self):
        return self.first_name + " " + self.last_name


if __name__ == '__main__':


    studentset = StudentSet("Example_student_list")

    students = []
    students.append(Student('20022872', 'Eric', 'Leuty'))
    students.append(Student('00000001', 'Thing', 'One'))
    students.append(Student('00000002', 'Thing', 'Two'))
    students.append(Student('00000003', 'Thing', 'Three'))
    students.append(Student('00000004', 'Thing', 'Four'))
    students.append(Student('00000005', 'Thing', 'Five'))
    students.append(Student('00000006', 'Thing', 'Six'))
    students.append(Student('00000007', 'Thing', 'Seven'))



    for student in students:
        studentset.add_student(student)

    studentset.print()
    studentset.save()

    studentset = StudentSet.load("Example_student_list")
    studentset.print()