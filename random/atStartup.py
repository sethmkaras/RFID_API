import os
import time
import subprocess, shlex
from subprocess import *
command = "ssh -t -t sethkara@timberlake.cse.buffalo.edu "

#proc = subprocess.call(command, shell=True)
proc = subprocess.Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE);
proc.communicate('exit')



