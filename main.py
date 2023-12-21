import numpy as np
from itertools import permutations
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
  #x = lambda a: "."+"".join([b+"#" for i in range(a)])+"."
  x = lambda a: "".join([b+"#" for i in range(a)])
  return list(map(x, numlst))

springMap, springNum = readFile2Data()
print(springMap)
print(springNum)

b=""
#x = lambda a: "."+"".join([b+"#" for i in range(a)])+"."
x = lambda a: "".join([b+"#" for i in range(a)])
#print(x(3))
#print(list(map(x, [1,1,3])))

length = len(springMap)

for i in range(length):
  #changing the lists to np.arrays so that I can use where function to find where the ?s are and where 1s are etc. 
  brokenMap = np.array([c for c in springMap[i]])
  #print(brokenMap)
  #z = input("enter a key: ")
  xq = np.array(np.where(brokenMap == "?"))[0]
  #print(xq)
  #z = input("enter a key: ")
  xh = np.array(np.where(brokenMap == "#"))[0]
  xd = np.array(np.where(brokenMap == "."))[0]
  print(f"xq = {xq}, xh = {xh}, xd = {xd}")
  z = input("enter a key: ")
  #print(f"xq = {xq}, xh = {xh}, xd = {xd}")
  #z = input("enter a key: ")

  


  
  
  
  


