from sys import *
from os import path

def teacher(lastname, f_in):
    for line in f_in.readlines():
          line = line.split(",")
          if line[6] == lastname:
             line = line[0] + "," + line[1]
             print(line)
def student(lastname, f_in, bus):
    if bus == 'N':
       for line in f_in.readlines():
          line = line.split(",")
          if line[0] == lastname:
             line = line[0] + "," + line[1] + "," + line[2] + "," + line[3] + "," + line[6] + "," + line[7]
             line = line.split("\n")
             print(line[0])
    else:
       for line in f_in.readlines():
          line = line.split(",")
          if line[0] == lastname and line[4] == bus:
             line = line[0] + "," + line[1] + "," + line[2] + "," + line[3] + "," + line[4] + "," + line[6] + "," + line[7]
             line = line.split("\n")
             print(line[0])
def grade(grade, f_in, gpa):
   if gpa == 'N':
      for line in f_in.readlines():
          line = line.split(",")
          if line[2] == grade:
             line = line[0] + "," + line[1]
             print(line)
   elif gpa == 'H':
      lt = []
      highest = 0.0
      hl = []
      for line in f_in.readlines():
          line = line.split(",")
          if line[2] == grade:
             lt.append(line)
      for line in lt:
         if float(line[5]) > highest:
             highest = float(line[5])
             hl = line
      hl = hl[0] + "," + hl[1] + "," + hl[4] + "," + hl[5] + "," + hl[6] + "," + hl[7]
      hl = hl.split("\n")
      print(hl[0])
   elif gpa == 'L':
      lt = []
      lowest = 4.0
      ll = []
      for line in f_in.readlines():
          line = line.split(",")
          if line[2] == grade:
             lt.append(line)
      for line in lt:
         if float(line[5]) < lowest:
             lowest = float(line[5])
             ll = line
      ll = ll[0] + "," + ll[1] + "," + ll[4] + ","+ ll[5] + "," + ll[6] + "," + ll[7]
      ll = ll.split("\n")
      print(ll[0])
def bus(route, f_in):
    for line in f_in.readlines():
          line = line.split(",")
          if line[4] == route:
             line = line[0] + "," + line[1] + "," + line[2] + "," + line[3]
             print(line)
def average(gradenumber,f_in):
    total = 0
    count = 0
    studentsGrade = []
    for student in f_in:
        student = student.split(",")
        if student[2] == gradenumber:
            studentsGrade.append(student[5])
    for student in studentsGrade:
        total += float(student)
        count += 1
    if count == 0:
        return 0
    average = total / count
    average = round(average,2)
    print("Grade level: " + str(gradenumber))
    print("Average GPA: " + str(average))
    

def info(f_in):
   classSize = [0]*7
   for student in f_in.readlines():
        student = student.split(",")
        if student[2] == '0':
           classSize[0] += 1
        if student[2] == '1':
           classSize[1] += 1 
        if student[2] == '2':
           classSize[2] += 1
        if student[2] == '3':
           classSize[3] += 1
        if student[2] == '4':
           classSize[4] += 1
        if student[2] == '5':
           classSize[5] += 1
        if student[2] == '6':
           classSize[6] += 1
   for i in range(0,7):
      print("Grade "+str(i)+":  " +str(classSize[i]))

def query(cmd, f_in):
    if cmd[0] == 'S:':
      if len(cmd) == 2:
         student(cmd[1], f_in, 'N')
      elif len(cmd) == 3:
         student(cmd[1], f_in, cmd[2])
    elif cmd[0] == 'T:':
      teacher(cmd[1], f_in)
    elif cmd[0] == 'B:':
      bus(cmd[1], f_in)
    elif cmd[0] == 'G:':
      if len(cmd) == 2:
         grade(cmd[1], f_in, 'N')
      elif len(cmd) == 3:
        grade(cmd[1], f_in, cmd[2])
    elif cmd[0] == 'A:':
      average(cmd[1], f_in)
    elif cmd[0] == 'I':
      info(f_in)
    elif cmd[0] == 'Q':
       return False
    return True

def main():
    print("Welcome to school search.")
    while True:
       if path.exists("students.txt")==False:
           print("File students.txt not found")
           exit(1)
       f_in = open('students.txt', 'r')
       for line in f_in.readlines():
          line = line.split(",")
          if len(line) != 8:
            print("Wrong format for students.txt")
            f_in.close()
            exit(1)
       f_in.close()
       f_in = open('students.txt', 'r')
       command = input("Enter a search command: ")
       cmd = command.split(" ") 
       check = query(cmd, f_in)
       f_in.close()
       if check == False:
          break


if __name__=='__main__':
   main()
