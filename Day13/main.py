import numpy as np

f=open("day13_input.txt", "r")

def readFile2Data(f):
  data=[]
  for line in f:
    line=line.strip()
    if len(line)!=0:
      data.append(line.strip())
    else:
      return data
  return data

def findMirror(data):
  length = len(data)
  #print(f"length = {length}")
  for m in range(1,length):
    #print(data[m])
    if data[m-1]==data[m]:
      print(f"found mirror between {m-1} and {m} ")
      z = input("enter a key: ")
      return m
  return False

def findRefln(m, data):  
  #print(m-1, m)
  up = data[:m] 
  #print(f"before reversing up =  {up}")
  up = up[::-1]
  print(f"after reversing {up}")
  down = data[m:]
  print(f"down =  {down}")
  lenUp,lenDown = len(up), len(down)
  small = min (lenUp, lenDown)
  #print(f" small = {small}")
  count = 0
  for j in range(small):
    if up[j] != down[j]: # need to go all the way to the end
      if lenDown>1:
        data2 = down[::]
        m2 = findMirror(data2)
        return findRefln(m2,data2)
        #print("not mirror")
        #z = input("enter a key: ") 
      else: return False
  if lenUp!=1:
    return lenUp
  else: return 0

def getTransData(data):
  #print(data)
  #z = input("enter a key: ")
  data = np.array([list(line) for line in data])
  #print(data)
  #z = input("enter a key: ")
  r,c = data.shape
  #print(f"r,c = {r},{c}")
  data = data.transpose()
  r,c = data.shape
  #print(f"r,c = {r},{c}")
  #print(data)
  #z = input("enter a key: ") 
  data = ["".join(line) for line in data]
  #print(data)
  #z = input("enter a key: ") 
  return data

count = 0
sumTot = 0
  
while True:
  data = readFile2Data(f)
  if len(data)==0:
    print("reached the end of file")
    break
  else:
    for ro1col2 in range(2):
      print(f"rol1col2 = {ro1col2} and sumTot = {sumTot}")
      #z = input("enter a key: ")
      m = findMirror(data)
      #print(f"m = {m}")
      #z = input("enter a key: ")
      if m:
        count = findRefln(m, data) 
        if not count: 
          data = getTransData(data)
        else:
          #how do I handle the recursion happening here? 
          #print(f"m, count = {m, count} and we have a mirror")
          sumTot += 100*count if ro1col2 == 0 else sumTot+count
          print(f"m={m}, count={count} and sumTot={sumTot} at rol1col2 = {ro1col2}") 
          z = input("enter a key: ")
          break
      else:
        data = getTransData(data)
    
      #print(f"rol1col2 = {ro1col2} and sumTot = {sumTot}")
      #z = input("enter a key: ")
  
    
    """data = np.array([list(line) for line in data])
    print(data)
    z = input("enter a key: ")
    r,c = data.shape
    for i in range(1,r):
      if "".join(data[i-1]) == data[i]:
        print(f"found mirror between {i-1} and {i+1} ")
        z = input("enter a key: ")
    """
  
  

  

#print(data)
print(sumTot)
    
f.close()
