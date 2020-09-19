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
      print("HI")
    elif cmd[0] == 'I:':
      print("HI")
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
