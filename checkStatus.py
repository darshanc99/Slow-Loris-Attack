#Import Dependencies
import os, time

f = open('config.txt','r+')
target = f.read()
command = "http " + target

while True:
    os.system(command)
    time.sleep(10)
