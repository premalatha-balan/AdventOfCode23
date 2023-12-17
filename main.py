import numpy as np
from itertools import combinations
import math


def readFile2Data():
  f=open("testdataday12.txt", "r")
  springNum, springMap =[[]],[[]]
  numstr = [i for i in range(9)]
  for line in f:
    line = line.strip()
    for i in line:
      print(f"line = {line}")
      row = [c for c in line if c=="." or c=="#" or c=="?"] #the handle has moved to the end. so nothing there to extract from the line
      print(f"row = {row}")
      z = input("enter a key: ")
      springMap.append(row)
      row = [int(c) for c in line if c in numstr]
      print(f"row = {row}")
      z = input("enter a key: ")
      springNum.append(row)
  f.close
  return springMap, springNum


springMap, springNum = readFile2Data()
for i in range(len(springMap)):
  print(f"{springMap[i]}, {springNum[i]}")
  z = input("enter a key: ")
  


