from sys import *
#Working on Info,Average
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
      print("HI")
    elif cmd[0] == 'G:':
      print("HI")
    elif cmd[0] == 'A:':
      average(cmd[1],f_in)
    elif cmd[0] == 'I:':
      info(f_in)
    elif cmd[0] == 'Q:':
       return False
    else:
       exit(1)
    return True

def main():
    print("Welcome to school search.")
    while True:
       f_in = open('students.txt', 'r')
       command = input("Enter a search command: ")
       cmd = command.split(" ") 
       check = query(cmd, f_in)
       f_in.close()
       if check == False:
          break


if __name__=='__main__':
   main()
