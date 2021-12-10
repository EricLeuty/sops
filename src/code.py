import os
import json
from pathlib import Path

#Holds a unique set of behavior codes in a dictionary
class CodeSet(object):
    def __init__(self, name, codes=None):
        self.name = name
        if codes is not None:
            self.codes = codes
        else:
            self.codes = {}


    def add_code(self, code):
        try:
            self.codes.update({code.code_name: code.data})
        except:
            print("Error: failed to add code to code set.")


    def remove_code(self, code_name):
        try:
            self.codes.pop(code_name)
        except:
            print("Error: failed to delete code.")


    def save(self):
        codeset_path = Path(os.getcwd()).parent / "Codes" / (self.name + ".json")
        codes_json = json.dumps(self.codes)
        f = open(codeset_path, "w")
        f.write(codes_json)
        f.close()


    def load(codeset_name):
        codeset_path = Path(os.getcwd()).parent / "Codes" / (codeset_name + ".json")
        try:
            f = open(codeset_path, "r")
            codes = json.loads(f.readline())
            f.close()
            return CodeSet(codeset_name, codes)
        except FileNotFoundError:
            print("Error: file not found")


    def print(self):
        for key, value in self.codes.items():
            print(key, ' : ', value)


class Code(object):
    def __init__(self, code_name, description=None, icon_path=None):
        self.code_name = code_name
        self.data = {
            "description": description,
            "iconPath": icon_path
        }


if __name__ == '__main__':
    codes = []
    codes.append(Code("L", description="Listening to TA, video or student presentation as a class."))
    codes.append(Code("Lab", description="Performing the lab activity."))
    codes.append(Code("TQ", description="Taking a test or quiz."))
    codes.append(Code("SQ", description="Asking the TA a lab-related question with entire class listening."))
    codes.append(Code("1o1-SQ", description="Individual student or a group of students asking the TA a lab-related question."))
    codes.append(Code("WC", description="Engaging in a whole class discussion often facilitated by TA."))
    codes.append(Code("Prd", description="Making a prediction about the outcome of a demo or experiment."))
    codes.append(Code("SP", description="Giving a presentation."))
    codes.append(Code("SI", description="Initiating one-on-one interaction with the TA."))
    codes.append(Code("SL", description="Leaving the lab for the day."))
    codes.append(Code("W", description="Waiting."))
    codes.append(Code("O", description="Other."))

    codeset = CodeSet("LOPUS_student_behavior")

    for code in codes:
        codeset.add_code(code)

    codeset.print()
    codeset.save()

