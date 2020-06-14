from secret import *

from subprocess import check_output

def openEpitech(secret):

    if secret != getSecret("Epitech"):
        return
    command = "start firefox http://viveepitech.pythonanywhere.com/2021"
    check_output(command, shell=True)
