
#Learn to read this data from the file
#Time:        42     89     91     89
#Distance:   308   1170   1291   1467

getDist = lambda t: [(t-i)*i for i in range(1,t)] #getDist is a function

boatRace = lambda tupIn: len(list(filter(lambda a: True if a>tupIn[1] else False, getDist(tupIn[0]))))

data = [(42,308), (89,1170), (91,1291), (89,1467)]

result=1
for i in range(len(ways)):
  result*=ways[i]
print(result)


