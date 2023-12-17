import numpy as np
from itertools import combinations
import math


def readFile2Data():
  f=open("testdataday12.txt", "r")
  springNum, springMap =[],[]
  numstr = [i for i in range(9)]
  count = 0
  for line in f:
    line = line.strip("")
    #print(f"line = line")
    start = max(line.rfind("#"), line.rfind("?"), line.rfind("."))
    row = line[start+1: ].strip().split(",")
    row = [int(r) for r in row]
    springNum.append(row)
    #print(f"springNum = {springNum}")
    #z = input("enter a key: ")
      
    row = [line[c] for c in range(start+1)]
    #print(f"row = {row}")
    #z = input("enter a key: ")
    springMap.append(row)
    #print(f"springMap = {springMap}")
    #z = input("enter a key: ")
  f.close
  return springMap, springNum


springMap, springNum = readFile2Data()

print(len(springMap))
print(len(springNum))
z = input("enter a key: ")

for i in range(len(springMap)):
  print(f"{springMap[i]}, {springNum[i]}")
  z = input("enter a key: ")
  


