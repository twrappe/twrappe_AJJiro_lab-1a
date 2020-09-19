from sys import *

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
      #average()
      print(2)
    elif cmd[0] == 'I:':
      #info()
      print(3)
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
