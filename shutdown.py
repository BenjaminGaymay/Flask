from secret import *

from subprocess import check_output

def shutdownComputer(secret):

    if secret != getSecret("Shutdown"):
        return
    command = "shutdown /s /t 05"
    check_output(command, shell=True)


def standByComputer(secret):

    if secret != getSecret("M1s33nV31lle"):
        return

    command = "rundll32.exe powrprof.dll,SetSuspendState 0,1,0"
    check_output(command, shell=True)
