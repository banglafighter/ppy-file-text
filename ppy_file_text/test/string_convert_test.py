from ppy_file_text import StringUtil


def test1():
    string_collection = [
        "Student",  "tEacher", "Student_Teacher", "student99", "99student",
        "PWeb   Student", "my name is"
    ]
    for name in string_collection:
        print(f"Original: {name}, Display Name : {StringUtil.human_readable(name)}, Class Name: {StringUtil.py_class_name(name)}, File Name: {StringUtil.py_underscore_name(name)}, Pacakge Name: {StringUtil.py_hyphen_name(name)}")


test1()
