import subprocess
import os
args = "devcpp.exe -c " + os.getcwd() + "\\config"
subprocess.call(args)