import os
import json
from pathlib import Path

#Holds a unique set of behavior codes in a dictionary
class CodeSet(object):
    def __init__(self, name, codes=None):
        if not isinstance(name, str):
            raise CodeSetError("codeset_name", name, str)
        self.name = name
        if codes is not None:
            if not isinstance(codes, dict):
                raise CodeSetError("codes", codes, dict)
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
        codeset_path = Path(os.getcwd()).parent / "Codesets" / (self.name + ".json")
        codes_json = json.dumps({'name': self.name, 'codes': self.codes})
        f = open(codeset_path, "w")
        f.write(codes_json)
        f.close()



    def load(codeset_name):
        codeset_path = Path(os.getcwd()).parent / "Codesets" / codeset_name
        try:
            f = open(codeset_path, "r")
            codeset = json.loads(f.readline())
            f.close()
            return CodeSet(codeset['name'], codeset['codes'])
        except FileNotFoundError:
            print("Error: file not found")

    def load_from_path(codeset_path):
        try:
            f = open(codeset_path, "r")
            codeset = json.loads(f.readline())
            f.close()
            return CodeSet(codeset['name'], codeset['codes'])
        except FileNotFoundError:
            print("Error: file not found")


    def print(self):
        for key, value in self.codes.items():
            print(key, ' : ', value)

class CodeSetError(Exception):
    def __init__(self, error_type, value, expected_type):
        self.message = "CodeSetError: {} must be a {}, but {} was given.".format(error_type, expected_type,
                                                                                     type(value))
        super().__init__(self.message)

    def __str__(self):
        return self.message


class CodeItem(object):
    def __init__(self, code_name, description=None, icon_path=None):

        if not isinstance(code_name, str):
            raise CodeItemError("code_name", code_name)
        if not isinstance(description, str):
            raise CodeItemError("description", description)
        self.code_name = code_name
        self.data = {
            "description": description,
            "iconPath": icon_path
        }

    def __str__(self):
        return self.code_name

class CodeItemError(Exception):
    def __init__(self, error_type, value):
        self.message = "CodeItemError: {} must be a string, but {} was given.".format(error_type, type(value))
        super().__init__(self.message)

    def __str__(self):
        return self.message

def TestCodeItem():
    print("Test 1")
    code_name_1 = "code_1"
    description_1 = "This is the description for code_1."
    code_item_1 = CodeItem(code_name_1, description=description_1)
    if str(code_item_1) == code_name_1:
        print("passed")

    print("Test 2")
    code_name_2 = 2
    description_2 = description_1
    try:
        code_item_2 = CodeItem(code_name_2, description_2)
    except CodeItemError:
        print("passed")

    print("Test 3")
    code_name_3 = "code_name_3"
    description_3 = 3
    try:
        code_item_3 = CodeItem(code_name_3, description_3)
    except CodeItemError:
        print("passed")


def TestCodeSet():
    code_item_1 = CodeItem("code_name_1", description="This is the description for code_1.")
    code_item_2 = CodeItem("code_name_2", description="This is the description for code_2.")
    code_item_3 = CodeItem("code_name_3", description="This is the description for code_3.")
    code_item_bad = "This is not a CodeItem"

    print("Test 1")
    codeset_name_1 = "codeset_name_1"
    codeset_1 = CodeSet(codeset_name_1)
    print("passed")

    print("Test 2")
    codeset_name_2 = 2
    try:
        codeset_2 = CodeSet(codeset_name_2)
    except CodeSetError:
        print(CodeSetError)
        print("passed")





def LOPUS_Codes():

    codes = []
    codes.append(CodeItem("L", description="Listening to TA, video or student presentation as a class."))
    codes.append(CodeItem("Lab", description="Performing the lab activity."))
    codes.append(CodeItem("TQ", description="Taking a test or quiz."))
    codes.append(CodeItem("SQ", description="Asking the TA a lab-related question with entire class listening."))
    codes.append(CodeItem("1o1-SQ",
                          description="Individual student or a group of students asking the TA a lab-related question."))
    codes.append(CodeItem("WC", description="Engaging in a whole class discussion often facilitated by TA."))
    codes.append(CodeItem("Prd", description="Making a prediction about the outcome of a demo or experiment."))
    codes.append(CodeItem("SP", description="Giving a presentation."))
    codes.append(CodeItem("SI", description="Initiating one-on-one interaction with the TA."))
    codes.append(CodeItem("SL", description="Leaving the lab for the day."))
    codes.append(CodeItem("W", description="Waiting."))
    codes.append(CodeItem("O", description="Other."))

    codeset = CodeSet("LOPUS_student_behavior")

    for code in codes:
        codeset.add_code(code)

    codeset.print()
    codeset.save()


if __name__ == '__main__':
    LOPUS_Codes()
    TestCodeSet()

