import os
import pickle
from pathlib import Path
from observation import DataSet
from codes import CodeSet


class Session(DataSet):
    def __init__(self, name, code_set=None, path_media=None, student_set=None):
        super().__init__()
        self.name = name
        self.codeset = code_set
        self.path_media = path_media
        self.student_set = student_set

    def save(self):
        session_path = Path(os.getcwd()).parent / "Sessions" / self.name
        try:
            f = open(session_path, "wb")
            pickle.dump(self, f)
            f.close()
        except:
            print("Error: file not found.")


    def load(session_name):
        session_path = Path(os.getcwd()).parent / "Sessions" / session_name
        print(session_path)
        try:
            f = open(session_path, "rb")
            session = pickle.load(f)
            f.close()
            return session
        except FileNotFoundError:
            print("Error: file not found.")


    def print(self):
        print(self.name)


class SessionSet(object):
    def __init__(self):
        self.sessions = {}


    def add_session(self, session):
        self.sessions.update({session.name: session})


    def remove_session(self, session_name):
        self.sessions.pop(session_name)

    def load(self):
        print("")

    def save(self):
        print("")



if __name__ == '__main__':
    students = ["student1", "student2", "student3", "student4", "student5",
                "student6", "student7", "student8", "student9", "student10"]
    media = Path(os.getcwd()).parent / "Media" / "LOPUS.mp4"
    codeset = CodeSet.load("LOPUS_student_behavior")
    session1 = Session("Queens_LOPUS", code_set=codeset, path_media=media, student_set=students)
    session1.save()