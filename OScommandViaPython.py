#Running Os command via Python
import os
import subprocess

if __name__ == "__main__" :
    rd = os.popen("git --version").read()
    print(rd)
    os.system("npm --version")
    os.system("node --version")
    returned_output = subprocess.check_output("date")
    print(returned_output)
    subprocess.call("date")