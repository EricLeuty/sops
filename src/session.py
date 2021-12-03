import pickle
from code import *
from behaviorData import *


class Session(object):
    def __init__(self, name, codeSet=None, mediaPaths=None, studentSet=None):
        self.name = name
        self.code_set = codeSet
        self.mediaPaths = mediaPaths
        self.studentSet = studentSet
        self.data = BehaviorSet()


    def setCodeSet(self, codeSet):
        if(isinstance(codeSet, CodeSet)):
            self.code_set = codeSet


    def addDataPoint(self, dataPoint):
        self.data.addDataPoint(dataPoint)


    def save(self):
        fPath = Path(os.getcwd()).parent / "Sessions" / self.name
        try:
            f = open(fPath, "wb")
            pickle.dump(self, f)
            f.close()
        except:
            print("Error: file not found.")


    def load(sessionName):
        fPath = Path(os.getcwd()).parent / "Sessions" / sessionName
        try:
            f = open(fPath, "rb")
            session = pickle.load(f)
            f.close()
            return session
        except FileNotFoundError:
            print("Error: file not found.")


    def print(self):
        print(self.name)


if __name__ == '__main__':
    session1 = Session.load("test_session")
    session1.print()