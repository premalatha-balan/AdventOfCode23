
def readFile2Data():
  f=open("day6_input.txt", "r")
  time = f[0].find(":").strip()
  print(time)
  
 
  f.close
  return(data)

#read this data from the file removing all spaces and joining them up. Will do once I have got the solution. easy to do.
#Time:        42     89     91     89
#Distance:   308   1170   1291   1467


#getDist = (lambda t, d: [(t-i)*i for i in range(1,int(t/2+1)) if (t-i)*i<d])  #getDist is a function
readFile2Data
y = input("enter a key: ")

getDist = lambda t, d: sum((t - i) * i < d for i in range(1, int(t / 2) + 1))

data=(42899189, 308117012911467) #part2 #

ways = getDist(data[0], data[1])
print(ways)

#ways = list(map(boatRace, data)) #part 1
#ways = boatRace(data) #part 2
#ways = len(getDist(data[0], data[1]))
#print(ways)

"""result=1
for i in range(len(ways)):
  result*=ways[i]
print(result)"""

"""
getDist = lambda t, d: sum((t - i) * i < d for i in range(1, int(t / 2) + 1))
data = (42899189, 308117012911467)
ways = getDist(data[0], data[1])
print(ways)"""

