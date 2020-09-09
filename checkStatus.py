#Import Dependencies
import os, time

f = open('config.txt','r+')
target = f.read()
command = "time curl -I " + target + " | grep HTTP"

while True:
    resp = os.system(command)
    print("\n\n")
    time.sleep(10)
