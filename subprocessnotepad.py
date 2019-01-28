import subprocess as sp
import time
import pyautogui
programName = "notepad.exe"

sp.Popen(programName)
time.sleep(1)
pyautogui.typewrite("Welcome to python programming!\n")
pyautogui.typewrite("----------------------------------\n")

string1 = "There are two ways of installing third party libraries\n\n"
string2 = "1. Manual download and install\n"
string3 = "2. pip tool or easy_install tool\n"

string4 = "All the third party libraries are available in\n\n"
string5 = "www.pypi.python.org\n"

liststr1 = list(string1)
liststr2 = list(string2)
liststr3 = list(string3)
liststr4 = list(string4)
liststr5 = list(string5)


for char in liststr1:
    time.sleep(0.05)
    pyautogui.typewrite(char)


for char in liststr2:
    time.sleep(0.05)
    pyautogui.typewrite(char)


for char in liststr3:
    time.sleep(0.05)
    pyautogui.typewrite(char)


for char in liststr4:
    time.sleep(0.05)
    pyautogui.typewrite(char)


     
