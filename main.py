
def readFile2Data():
  f=open("day5_input.txt", "r")
  
  #reading the file and storing it in a list
  inData = [line.strip() for line in f if (line != "" and line != " " and line != "\n")]
  #print(inData)
  
  seeds = inData[0].split()
  seeds.remove("seeds:")
  seeds = [int(i) for i in seeds]
  #print(seeds)
  seedPairs = []
  for i in range(0,len(seeds),2):
    #print(seeds[i], seeds[i+1])
    pair=(seeds[i], seeds[i+1])
    #print(pair)
    seedPairs.append(pair)
  #print(seedPairs)
  
  seed2SoilMap = inData[2:inData.index("soil-to-fertilizer map:")]
  seed2SoilMap = [line.split() for line in seed2SoilMap]
  seed2SoilMap = [[int(i) for i in line] for line in seed2SoilMap]
  #print(seed2SoilMap)
  
  soil2FertlMap = inData[inData.index("soil-to-fertilizer map:")+1:inData.index("fertilizer-to-water map:")]
  soil2FertlMap = [line.split() for line in soil2FertlMap]
  soil2FertlMap = [[int(i) for i in line] for line in soil2FertlMap]
  #print(soil2FertlMap)
  
  fertl2WaterMap = inData[inData.index("fertilizer-to-water map:")+1:inData.index("water-to-light map:")]
  fertl2WaterMap = [line.split() for line in fertl2WaterMap]
  fertl2WaterMap = [[int(i) for i in line] for line in fertl2WaterMap]
  #print(f"fertl2WaterMap = {fertl2WaterMap}")
  
  water2LightMap  = inData[inData.index("water-to-light map:")+1:inData.index("light-to-temperature map:")]
  water2LightMap = [line.split() for line in water2LightMap]
  water2LightMap = [[int(i) for i in line] for line in water2LightMap]
  
  #print(f"water2LightMap = {water2LightMap}")
  
  light2TempMap = inData[inData.index("light-to-temperature map:")+1:inData.index("temperature-to-humidity map:")]
  light2TempMap = [line.split() for line in light2TempMap]
  light2TempMap = [[int(i) for i in line] for line in light2TempMap]
  #print(f"light2TempMap = {light2TempMap}")
  
  temp2HumidMap = inData[inData.index("temperature-to-humidity map:")+1:inData.index("humidity-to-location map:")]
  temp2HumidMap = [line.split() for line in temp2HumidMap]
  temp2HumidMap = [[int(i) for i in line] for line in temp2HumidMap]
  #print(f"temp2HumidMap = {temp2HumidMap}")
  
  humid2LocMap = inData[inData.index("humidity-to-location map:")+1:]
  humid2LocMap = [line.split() for line in humid2LocMap]
  humid2LocMap = [[int(i) for i in line] for line in humid2LocMap]
  #print(f"humid2LocMap = {humid2LocMap}")

  f.close
  return(seedPairs, seed2SoilMap, soil2FertlMap, fertl2WaterMap, water2LightMap, light2TempMap, temp2HumidMap,humid2LocMap)


xCorres = lambda a, b, start, end: a if a<start or a>end else b+(a-start)


#need to check the end of the range is still in match.

def checkRange(pair, mapData):
  #The range is start+range-1
  
  for line in mapData:
    start, end = line[1], line[1]+line[2]-1 
    startPair, endPair = pair[0], pair[0]+pair[1]-1

    if startPair>=start:
      if endPair<=end: # seed range is fully inside
        matched = xCorres(startPair, line[0], start, end)
        match = (matched, pair[1]) # tuple match is a soil correspondent tuple
        return match, tuple()
      else: #endPair>end:
        if startPair< end:
          endMatch = line[2]+line[1]-matched #+1 & -1 cancel out
          matched = xCorres(startPair, line[0], start, end)
          match = (matched, endMatch)
          appendPair = (endMatch+1,  endPair-end) #appending unmatched bottom bit as seed and range
          return match, appendPair
        elif startPair == end:
          endMatch==0
          matched = xCorres(startPair, line[0], start, end)
          match = (matched, 0)
          return match, tuple()
        else: return (pair[0], pair[1]), tuple()
    else: #startPair<start
      if endPair<start:
        match = (pair[0], pair[1])
        return match, tuple()
      elif endPair=start:
        matched = xCorres(endPair, line[0],start, end)
        match=(matched, 0)
        return match, tuple()
      else: #endPair>start:
        appendPair = (startPair, startPair-start)
        matched = xCorres(start, line[0], start, end)
        endMatch = endPair-start+1
        match = (matched, endMatch), 
        return match, appendPair

  return match(pair[0], pair[1]), tuple()


#main 
seedPairs, seed2SoilMap, soil2FertlMap, fertl2WaterMap, water2LightMap, light2TempMap, temp2HumidMap, humid2LocMap =  readFile2Data()

soilPairs=[]
fertlPairs=[]
waterPairs=[] 
lightPairs=[]
tempPairs=[]
humidPairs=[]
locationPairs=[]


locations=[]
#correspond=[]
for pair in seedPairs:
  print(pair)
  #corres=[]
  #corres.append(seed)
    #print(seed)
  s2SMatch = checkRange(pair[0], seed2SoilMap)
  #corres.append(s2SMatch)
  #print(f"s2SMatch = {s2SMatch}")
  s2FMatch = checkRange(s2SMatch, soil2FertlMap)
  #corres.append(s2FMatch)
  #print(f"s2FMatch = {s2FMatch}")
  f2WMatch = checkRange(s2FMatch, fertl2WaterMap)
  #corres.append(f2WMatch)
  #print(f"f2WMatch = {f2WMatch}")
  w2LMatch = checkRange(f2WMatch, water2LightMap)
  #corres.append(w2LMatch)
  #print(f"w2LMatch = {w2LMatch}")
  l2TMatch = checkRange(w2LMatch, light2TempMap)
  #corres.append(l2TMatch)
  #print(f"l2TMatch = {l2TMatch}")
  t2HMatch = checkRange(l2TMatch, temp2HumidMap)
  #corres.append(t2HMatch)
  #print(f"t2HMatch = {t2HMatch}")
  h2LMatch = checkRange(t2HMatch, humid2LocMap)
  locations.append(h2LMatch)
  print(locations)
  y=input("enter a key: ")
    #print(h2LMatch)
    #corres.append(h2LMatch)
    #correspond.append(corres)

print(min(locations))