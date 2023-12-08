
#Need to work on combining the pairs and reducing for loops

def readFile2Data():
  f=open("day5_input.txt", "r")
  
  #reading the file and storing it in a list
  inData = [line.strip() for line in f if (line != "" and line != " " and line != "\n")]
  
  seeds = inData[0].split()
  seeds.remove("seeds:")
  #print(f"seeds = {seeds} ")
  #y = input("enter a key: ")
  seeds = list(map(int, seeds))
  #print(f"seeds = {seeds} ")
  #y = input("enter a key: ")
  #print(seeds)
  seedPairs = [(seeds[i], seeds[i+1]) for i in range (0,len(seeds),2)]
  #print(f"seedPairs = {seedPairs}")
  #y = input("enter a key: ")
  seed2SoilMap = inData[2:inData.index("soil-to-fertilizer map:")]
  seed2SoilMap = [tuple(map(int, line.split())) for line in seed2SoilMap]
  #print(f"seed2SoilMap = {seed2SoilMap}")
  #y = input("enter a key: ")
  
  soil2FertlMap = inData[inData.index("soil-to-fertilizer map:")+1:inData.index("fertilizer-to-water map:")]
  soil2FertlMap = [tuple(map(int, line.split())) for line in soil2FertlMap]
  #print(soil2FertlMap)
  
  fertl2WaterMap = inData[inData.index("fertilizer-to-water map:")+1:inData.index("water-to-light map:")]
  fertl2WaterMap = [tuple(map(int, line.split())) for line in fertl2WaterMap]
  #print(f"fertl2WaterMap = {fertl2WaterMap}")
  
  water2LightMap  = inData[inData.index("water-to-light map:")+1:inData.index("light-to-temperature map:")]
  water2LightMap = [tuple(map(int, line.split())) for line in water2LightMap]
  #print(f"water2LightMap = {water2LightMap}")
  
  light2TempMap = inData[inData.index("light-to-temperature map:")+1:inData.index("temperature-to-humidity map:")]
  light2TempMap = [tuple(map(int, line.split())) for line in light2TempMap]
  #print(f"light2TempMap = {light2TempMap}")
  
  temp2HumidMap = inData[inData.index("temperature-to-humidity map:")+1:inData.index("humidity-to-location map:")]
  temp2HumidMap = [tuple(map(int, line.split())) for line in temp2HumidMap]
  #print(f"temp2HumidMap = {temp2HumidMap}")
  
  humid2LocMap = inData[inData.index("humidity-to-location map:")+1:]
  humid2LocMap = [tuple(map(int, line.split())) for line in humid2LocMap]
  #print(f"humid2LocMap = {humid2LocMap}")

  f.close
  return(seedPairs, seed2SoilMap, soil2FertlMap, fertl2WaterMap, water2LightMap, light2TempMap, temp2HumidMap,humid2LocMap)


xCorres = lambda a, b, start, end: b+(a-start) if (a>=start and a<=end) else a


def correspond(pair, destPair, sourcePair, mapData):
  #The range is start+range-1
  for line in mapData:
    start, end = line[1], xEnd(line[1], line[2]) 
    startPair, endPair = pair[0], xEnd(pair[0], pair[1])

    if startPair>=start:           
      if endPair<=end: # seed range is fully inside
        matched = xCorres(startPair, line[0], start, end)
        destPair.append((matched, pair[1])) # tuple match is a soil correspondent tuple
        #print(f"destPair = {(matched, pair[1])} at fully inside ")
      else: #endPair>end:
        if startPair< end:
          matched = xCorres(startPair, line[0], start, end)
          endMatch = end-startPair#+1 & -1 cancel out
          destPair.append((matched, endMatch))
          #print(f"destPair = {(matched, endMatch)} at end ")
        elif startPair == end:
          endMatch==0
          matched = xCorres(startPair, line[0], start, end)
          destPair.append((matched, 0))
        else:
          if (pair[0], pair[1]) not in destPair: destPair.append((pair[0], pair[1]))
    else: #startPair<start
      if endPair<start:
        if (pair[0], pair[1]) not in destPair: destPair.append((pair[0], pair[1]))
      elif endPair==start:
        matched = xCorres(endPair, line[0],start, end)
        destPair.append((matched, 0))
      else: #endPair>start:
        matched = xCorres(start, line[0], start, end)
        endMatch = endPair-start+1
        destPair.append((matched, endMatch))

tuple2starts = lambda tuplein : tuplein[0]
#tuple2data = lambda tuplein : a, b


#main 
seedPairs, seed2SoilMap, soil2FertlMap, fertl2WaterMap, water2LightMap, light2TempMap, temp2HumidMap, humid2LocMap =  readFile2Data()
#print(f"seedPairs = {seedPairs}")
#y = input("enter a key: ")

soilPairs=[]
fertlPairs=[]
waterPairs=[] 
lightPairs=[]
tempPairs=[]
humidPairs=[]
locationPairs=[]

xEnd = lambda start, range: start+range-1 #use this

def xCombineFindRange (tuple1, tuple2):
  firstEnd = xEnd(tuple1[0], tuple1[1])
  if firstEnd>=tuple2[0]:
    secondEnd = xEnd(tuple2[0], tuple2[1])
    range = secondEnd - tuple1[0]+1
    return(tuple1[0], range)

xCombine = lambda tuple1, tuple2: (tuple1[0], xCombineFindRange(tuple1, tuple2))


def xTidyTuples(tupleList):
  combined_tuples = map(lambda i: xCombine(tupleList[i], tupleList[i + 1]), range(0, len(tupleList), 2))
  new_tuple_list = list(zip(combined_tuples, tupleList[1::2]))

  return new_tuple_list


locations=[]
seedPairs.sort()
print(f"seedPairs = {seedPairs} ")
print(f"length of seedslist = {len(seedPairs)} ")
y=input("enter a key: ")
for seed in seedPairs:
  correspond(seed, soilPairs, seedPairs, seed2SoilMap)

print(f"soilPairs = {soilPairs} ")
print(f"length of soilPairs = {len(soilPairs)} ")
y=input("enter a key: ")
for soil in soilPairs:
  correspond(soil, fertlPairs, soilPairs, soil2FertlMap)

print(f"fertlPairs = {fertlPairs} ")
print(f"length of fertlPairs = {len(fertlPairs)} ")
y=input("enter a key: ")
for fertl in fertlPairs:
  correspond(fertl, waterPairs, fertlPairs, fertl2WaterMap)

print(f"waterPairs = {waterPairs} ")
print(f"length of waterPairs = {len(waterPairs)} ")
y=input("enter a key: ")
for water in waterPairs:
  correspond(water, lightPairs, waterPairs, water2LightMap)

print(f"lightPairs = {lightPairs} ")
print(f"length of lightPairs = {len(lightPairs)} ")
y=input("enter a key: ")
for light in lightPairs:
  correspond(light, tempPairs, lightPairs, light2TempMap)

print(f"tempPairs = {tempPairs} ")
print(f"length of tempPairs = {len(tempPairs)} ")
y=input("enter a key: ")
for temp in tempPairs:
  correspond(temp, humidPairs, tempPairs, temp2HumidMap)

print(f"humidPairs = {humidPairs} ")
print(f"length of humidPairs = {len(humidPairs)} ")
y=input("enter a key: ")
for humid in humidPairs:
  correspond(humid, locationPairs, humidPairs, humid2LocMap)

print("before locations print")
print(locationPairs)
y = input("enter a key: ")
locations = list(map(tuple2starts, locationPairs))

print(min(locations))
print("end of code")