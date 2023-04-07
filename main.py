# --------------------Student management system---------------

#----------------------|||----------------------------
import os
os.system('echo [Hello user welcome to student management system Follow given Instruction to run program] | powershell -command "& {Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak([Console]::In.ReadToEnd())}"')




print("Type add---To insert new student")
print("Type change---To change in existing marks")
print("Type result---To check result of student")
print("Type show---To get info of student")
print("Type delete---To delete info of student")
print("Type deleteAll---To delete all student")
print()

import json


MARKS_FILE = "marks.txt"

# Load marks from file or create an empty dictionary
if os.path.exists(MARKS_FILE):
  try:
    with open(MARKS_FILE, "r") as f:
      marks = json.load(f)
  except json.decoder.JSONDecodeError:
    # If there is an issue with the JSON data, create an empty dictionary
    marks = {}
else:
  marks = {}
from functools import reduce

while (True):

  user = input("--->")
  user = user.lower()
  marks1 = marks

  # --------------To add student------------------

  if user == "add":
    try:
      while True:
        student = input("Enter the name of student: ")
        if student == "":
          print("-----------Please enter the name-------")
        else:
          break
      while True:
        english = int(input("Enter the marks of english: "))
        Maths = int(input("Enter the marks of maths: "))
        science = int(input("Enter the marks of science: "))
        hindi = int(input("Enter the marks of hindi: "))
        sst = int(input("Enter the marks of sst: "))
        if english > 100 or Maths > 100 or science > 100 or hindi > 100 or sst > 100:
          print()
          print(
            "-------The given marks is either invalid or not entered correctly"
          )
          print("-----enter it again")
        else:
          break

      marks[student] = [english, Maths, science, hindi, sst]
      print("The student is successfully added")

      # Save marks to file
      with open(MARKS_FILE, "w") as f:
        json.dump(marks, f)
    except ValueError:
      print("Invalid input: please enter a number.")
    except:
      print("*********There is a some error***********")

      # ----------------To change student------------------

  elif user == "change":
    try:
      print("List of current students:")
      print(marks1.keys())
      student = input("Enter the name of student: ")
      if student in marks:
        english = int(input("Enter the marks of english: "))
        Maths = int(input("Enter the marks of maths: "))
        science = int(input("Enter the marks of science: "))
        hindi = int(input("Enter the marks of hindi: "))
        sst = int(input("Enter the marks of sst: "))
        marks[student] = [english, Maths, science, hindi, sst]
        print("Marks for", student, "updated to:", marks[student])
        with open(MARKS_FILE, "w") as f:
          json.dump(marks, f)
      else:
        print("Student", student, "not found in the list.")
    except:
      print("********There is a some error********")

      # -----------------To Exit loop----------------
  elif user == "exit":
    break

    # --------------------To check result-----------------
  elif user == "result":
    try:

      def average(a, b):
        return a + b

      result_list = []
      for x in marks:

        result_sum1 = reduce(average, marks[x])
        result_average1 = result_sum1 / 5
        if result_average1 < 33:
          result_list.append(False)
        else:
          result_list.append(True)
      result_count = result_list.count(True)
      print("The marks statistic----------------")
      print(f"Out of {len(marks)} student {result_count} is passed")
      print()
      print("The list of student that passed the exam")
      print()
      for student, passed in marks.items():
        if result_list[list(marks.keys()).index(student)]:
          print(student, passed)

      print()

      result_input = input("Enter the name of student: ")

      result_sum = reduce(average, marks[result_input])
      result_average = result_sum / 5
      if result_average < 33:
        print(f"{result_input} is failed with {result_average}%")
      else:
        print(f"{result_input} is pass with {result_average}%")
    except:
      print("**********There is some error*********")

      # --------------------To show info of student--------------
  elif user == "show":
    print(marks)

    # ------------------To delete student---------------------

  elif user == "delete":
    try:
      delete_stu = input("Enter the name of student you want to delete: ")
      if delete_stu in marks:
        del marks[delete_stu]
        print(f"{delete_stu} was successfully deleted")
        with open(MARKS_FILE, "w") as f:
          json.dump(marks, f)
      else:
        print("****The given student is not present in list***")
    except:
      print("*******There is some error*********")

    # ----------------------To give instruction----------------
  elif user == "ins":
    print("Type add---To insert new student")
    print("Type change---To change in existing marks")
    print("Type result---To check result of student")
    print("Type show---To get info of student")
    print("Type delete---To delete info of student")

  # ------------------To delete all student-------------

  elif user == "deleteall":
    confirm = input("Do you really want to delete every student ---Type yes")
    confirm = confirm.lower()
    if confirm == "yes":
      marks = {}
      with open(MARKS_FILE, "w") as f:
        json.dump(marks, f)
      print("The list is successfully deleted")
  else:
    print("please enter a valid input")
    from PyPDF2 import PdfWriter as w
    pdf=w()
    file=open("pavan.pdf","wb")
    for i in range():
        pdf.add_blank_page(219,297) #a4 size dimensions
    pdf.write(file)
    file.close()



