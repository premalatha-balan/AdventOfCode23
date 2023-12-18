#import numpy as np
from itertools import combinations
import math


def readFile2Data():
  f=open("testdataday12.txt", "r")
  springNum =[]
  springMap=[]
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
    row =line[:start+1].strip()
    #print(f"row = {row}")
    #z = input("enter a key: ")
    springMap.append(row)
    #print(f"springMap = {springMap}")
    #z = input("enter a key: ")
  f.close
  return springMap, springNum

def num2map(numlst):
  b=""
  x = lambda a: "."+"".join([b+"#" for i in range(a)])+"."
  return list(map(x, numlst))


springMap, springNum = readFile2Data()
print(springMap)
print(springNum)

b=""
x = lambda a: "."+"".join([b+"#" for i in range(a)])+"."
#print(x(3))
#print(list(map(x, [1,1,3])))

for i in range(len(springMap)):
  sMap = list(map(x, springNum[i]))
  for s in sMap:
    if s not in springMap[i]:
      print(s, springMap[i])
      z=input("enter a key")

z=input("enter a key")


length = len(springMap)
#changing the lists to np.arrays so that I can use where function to find where the ?s are and where 1s are etc. 
"""for i in range(length):
  springMap[i] = np.array(springMap[i])
  springNum[i] = np.array(springNum[i])
  xq = np.array(np.where(springMap[i] == "?"))[0]
  xh = np.array(np.where(springMap[i] == "#"))[0]
  xd = np.array(np.where(springMap[i] == "."))[0]
  print(xq, xh, xd)
  print(springNum[i])
  z = input("enter a key: ")"""
  
  
  
  


