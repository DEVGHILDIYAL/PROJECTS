import time;
import os
import sys
from keyboard import press

# os.system('cmd /k "color 02" ')
note1 = "Hey User Before Finding all possible combination for you system password we need some information answer all the question in y for yes or n for n format otherwise program will break\n\n"
note2 = "\n\nThat's great now all the required details are taken now tell file name in which i can store all the password\n\n"
note3 = '''\n\nloading...
boot system...
boot succesful...
establishing connection...
connection database...
connect...
loading...
entering safe mode...
connect unknown vpn...
vpn connected succesfully...
collection data...
all required connection done successfully...
reult...'''

def delayLine(note, speed=0.05):
    for i in range(len(note)):
        print(note[i], end="")
        sys.stdout.flush()
        time.sleep(speed)

delayLine(note1)
# print("Hey  User Before FInding all possible combination for you system password we need some information answer all the question in y for yes or n for n format otherwise program will break")

num = [0,1, 2,3,4,5,6,7,8,9]
upperChar = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowerChar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
special = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")" ,"_", "+", "-", "=", "{", "}", "[", "]", ":", '"', ";", "'", "<", ">", ".", "?", "/", "~", "`"]

isNum = input("Is your password contain numbers : ")
isUpperChar = input("Is your password contain Upper Case Alphabets :")
isLowerChar = input("Is your password contain Lower Case Alphabets :")
isSpecial = input("Is you password contain special char : ")
delayLine(note2)
fileName = input("Enter file name : ")
delayLine(note3, 0.1)

data = []
size = 0;

if(isNum == 'y'):
    for i in range(len(num)):
        data.append(num[i])
    size = size + len(num);
if(isUpperChar == 'y'):
    for i in range(len(upperChar)):
        data.append(upperChar[i])
    size = size + len(upperChar);
if(isLowerChar == 'y'):
    for i in range(len(lowerChar)):
        data.append(lowerChar[i])
    size = size + len(lowerChar);
if(isSpecial == 'y'):
    for i in range(len(special)):
        data.append(special[i])
    size = size + len(special);

n = 0;
fileName = fileName + ".txt"
file = open(fileName, "a")
# print(data)
for i in range(size):
    for j in range(size):
        for k in range(size):
            for l in range(size):
                # if(i != j & j != k & k!=i):
                n += 1
                password = str(data[i]) + str(data[j]) + str(data[k]) + str(data[l]) 
                file.write(str(password) + "\n")
                print(data[i], data[j], data[k], data[l], end="")
                print("                             |                       ", n)
                # time.sleep(0.05)
file.close()
print(f"Total {n} Combinations Found ")