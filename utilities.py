import os
import platform

clearType = "clear"
if (platform.system() == "Windows"):
    clearType = "cls"
clearScreen = lambda: os.system(clearType)

def sum_coords(arg1, arg2):
    xsum = arg1[0] + arg2[0]
    ysum = arg1[1] + arg2[1]
    sum = [xsum, ysum]
    return sum