#Running Os command via Python
import os

if __name__ == "__main__" :
    os.popen(
        'start notepad++ YourFile.txt'
        )
    os.system("notepad;cmd.exe") #Running cmd before notepad wont run notepad