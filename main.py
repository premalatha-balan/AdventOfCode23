"""
def readFile2Data():
  f=open("day5_input.txt", "r")
  
 
  f.close
  return(data)
"""
#read this data from the file
#Time:        42     89     91     89
#Distance:   308   1170   1291   1467


getDist = lambda t: [(t-i)*i for i in range(1,int(t/2+1))] #getDist is a function

print(getDist(42))
y = input("enter a key: ")

boatRace = lambda tupIn: len(list(filter(lambda a: True if a>tupIn[1] else False, getDist(tupIn[0]))))

#data = [(42,308), (89,1170), (91,1291), (89,1467)] #part1
data=(42899189, 308117012911467) #part2

#ways = list(map(boatRace, data)) #part 1
ways = boatRace(data) #part 2
print(ways)

"""result=1
for i in range(len(ways)):
  result*=ways[i]
print(result)"""



