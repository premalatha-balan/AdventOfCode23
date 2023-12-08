"""
def readFile2Data():
  f=open("day5_input.txt", "r")
  
 
  f.close
  return(data)
"""
#Learn to read this data from the file
#Time:        42     89     91     89
#Distance:   308   1170   1291   1467

getDist = lambda t: [(t-i)*i for i in range(1,t)]

def boatRace(tupleIn):
  dist=list(filter(lambda a: True if a>tupleIn[1] else False, getDist(tupleIn[0])))
  #print(dist)
  return len(dist)

data = [(42,308), (89,1170), (91,1291), (89,1467)]

ways = boatRace(data[0])
print(ways)

ways = list(map(boatRace, data))
print(ways)
result=1
for i in range(len(ways)):
  result*=ways[i]
print(result)

#Part1 needs cleaning up. Part 2 needs properly using some functions and recursions maybe

dist = getDist(42899189) #It is not as easy as I thought
print(dist)

