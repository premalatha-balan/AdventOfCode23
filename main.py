import numpy as np

f=open("testdataday13.txt", "r")

def readFile2Data(f):
  data=[]
  for line in f:
    line=line.strip()
    if len(line)!=0:
      data.append(line.strip())
    else:
      return data
  return data

def findMirror():
  length = len(data)
  print(f"length = {length}")
  for m in range(1,length):
    print(data[m])
    if data[m-1]==data[m]:
      print(f"found mirror between {m-1} and {m} ")
      z = input("enter a key: ")
      return m
  return False

def findRefln(m):  
  print(m-1, m)
  up = data[:m] 
  print(up)
  up = up[::-1]
  print(up)
  down = data[m:]
  small = min (len(up), len(down))
  print(f" small = {small}")
  count = 0
  for j in range(small):
    if up[j] == down[j]:
      count+=1
    else: 
      print("not mirror")
      return False
  z = input("enter a key: ")
  return count
  


while True:
  data = readFile2Data(f)

  m = findMirror()
  print(f"m = {m}")
  z = input("enter a key: ")
  if m:
    count = findRefln(m)
    print(m, count)
    z = input("enter a key: ")
  
  """data = np.array([list(line) for line in data])
  print(data)
  z = input("enter a key: ")
  r,c = data.shape
  for i in range(1,r):
    if "".join(data[i-1]) == data[i]:
      print(f"found mirror between {i-1} and {i+1} ")
      z = input("enter a key: ")
  """
  
  

  
  if len(data)==0:
    print("reached the end of file")
    break
#print(data)
    
f.close()