import os
import json
from pathlib import Path

#Holds a unique set of behavior codes in a dictionary
class CodeSet(object):
    def __init__(self, setName, codes=None):
        self.setName = setName
        if codes is not None:
            self.codes = codes
        else:
            self.codes = {}


    def addCode(self, code):
        try:
            self.codes.update({code.codeName: code.data})
        except:
            print("Error: failed to add code to code set.")


    def removeCode(self, codeName):
        try:
            self.codes.pop(codeName)
        except:
            print("Error: failed to delete code.")


    def save(self):
        fPath = Path(os.getcwd()).parent / "Codes" / (self.setName + ".json")
        codes_json = json.dumps(self.codes)
        f = open(fPath, "w")
        f.write(codes_json)
        f.close()


    def load(setName):
        fPath = Path(os.getcwd()).parent / "Codes" / (setName + ".json")
        try:
            f = open(fPath, "r")
            codes = json.loads(f.readline())
            f.close()
            return CodeSet(setName, codes)
        except FileNotFoundError:
            print("Error: file not found")


    def print(self):
        for key, value in self.codes.items():
            print(key, ' : ', value)


class Code(object):
    def __init__(self, codeName, description=None, iconPath=None):
        self.codeName = codeName
        self.data = {
            "description": description,
            "iconPath": iconPath
        }


if __name__ == '__main__':
    code1 = Code("CODE_1")
    code2 = Code("CODE_2")
    code3 = Code("CODE_3")
    code4 = Code("CODE_4")

    code_set = CodeSet("test_codes")

    code_set.addCode(code1)
    code_set.addCode(code2)
    code_set.addCode(code3)
    code_set.addCode(code4)
    code_set.print()
    code_set.save()
    code_set2 = CodeSet.load("test_codes")
    code_set2.print()