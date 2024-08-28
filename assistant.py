import os
import sys
from utils import get_file_paths

#These are the variables that need to be modified
foldername = "assistant"
personality = "assistant"
voicename = "Omen"
useEL = False           #EL = Eleven Labs 
useWhisper = False

#This checks if its an exe file or a python file
if getattr(sys, 'frozen', False):
    script_dir = os.path.dirname(os.path.abspath(sys.executable))   #try get rid of os.path.abspath() as it could be redundant
    while True:
        user_input = input("Are you using an Eleven Labs Voice (yes/no)?\n")
        if user_input == 'yes':
            voicename = input("What is the name of your Eleven Labs voice: ")
            useEL = True
            break
        elif user_input == "no":
            break
        else:
            print("Invalid Input, Please try again.\n")

else:
    script_dir = os.path.dirname(os.path.abspath(__file__))

foldername, personality, keys = get_file_path(script_dir,foldername,personality)