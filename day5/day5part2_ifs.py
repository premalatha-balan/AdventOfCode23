
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

"""def xCorres(a, b, start, end):
  print(f"a {a}, b {b} start {start}, end {end}")
  if a<start or a>end:
    print(f"a {a}, b {b} start {start}, end {end}")
    print(f"return {b+(a-start)}")
    y = input("enter a key: ")
    return b+(a-start)"""

#need to check the end of the range is still in match.

def correspond(pair, destPair, sourcePair, mapData):
  #The range is start+range-1
  for line in mapData:
    start, end = line[1], line[1]+line[2]-1 
    startPair, endPair = pair[0], pair[0]+pair[1]-1
    #print(f"start = {start}, end = {end}, startPair = {startPair}, endPair = {endPair}, line[0] {line[0]}, line {line}")
    #y = input("enter a key at the beginning: ")

    if startPair>=start:
      #print(f"yes, {startPair} >= {start}")
      #y = input("enter a key at if begin: ")
            
      if endPair<=end: # seed range is fully inside
        matched = xCorres(startPair, line[0], start, end)
        destPair.append((matched, pair[1])) # tuple match is a soil correspondent tuple
        #print("case: fully in")
        #print(f"matched = {matched}")
        #print(f"desPair = {destPair}")
        #y=input("enter a key: ")
      else: #endPair>end:
        #print(f"endPair {endPair} > end {end}")
        #y = input("enter a key at endpair is less than endSoil: ")
        
        if startPair< end:
          #print(f"startPair {startPair}, start {start}, end{end}, line[0] {line[0]} ")
          #y=input("enter a key: ")
          matched = xCorres(startPair, line[0], start, end)
          #print(f"matched = {matched}")
          #y=input("enter a key: ")
          endMatch = line[2]+line[1]-matched #+1 & -1 cancel out
          destPair.append((matched, endMatch))
          #sourcePair.append((end+1,  endPair-end)) #appending unmatched bottom bit as seed and range
          #print("case: unmatched bottom bit")
          #print(f"matched = {matched}")
          #print(f"destPair = {destPair}")
          #print(f"sourcePair = {(end+1, endPair-end)}")
          #y=input("enter a key: ")
        elif startPair == end:
          #print("no not a single line")
          endMatch==0
          matched = xCorres(startPair, line[0], start, end)
          destPair.append((matched, 0))
          #sourcePair.append((start, startPair-start))
          #print("case: just a line at startPair")
          #print(f"matched = {matched}")
          #print(f"destPair = {destPair}")
          #print(f"sourcePair = {(startPair+1, endPair-end)}")
          #y=input("enter a key: ")
        else:
          #print("yes, at fully bottom")
          if (pair[0], pair[1]) not in destPair: destPair.append((pair[0], pair[1]))
          #print(f"case: fully out bottom")
          #print(f"destPair = {destPair}")
          #y=input("enter a key: ")
    else: #startPair<start
      if endPair<start:
        if (pair[0], pair[1]) not in destPair: destPair.append((pair[0], pair[1]))
        #print(f"case: fully out at top")
        #print(f"destPair = {destPair}")
        #y=input("enter a key: ")
      elif endPair==start:
        matched = xCorres(endPair, line[0],start, end)
        destPair.append((matched, 0))
        #sourcePair.append((startPair, start-startPair))
        #print("case: just a line at endPair")
        #print(f"matched = {matched}")
        #print(f"destPair = {destPair} and sourcePair {startPair, start-startPair} ")
        #y=input("enter a key: ")
      else: #endPair>start:
        #print("case: unmatched top bit")
        #print(f"startPair {startPair} endPair {endPair}, start {start}, end{end}, line[0] {line[0]} ")
        #sourcePair.append((startPair, start-startPair))
        matched = xCorres(start, line[0], start, end)
        endMatch = endPair-start+1
        destPair.append((matched, endMatch))
        #print(f"matched = {matched}")
        #print(f"destPair = {destPair}, sourcePair = {(startPair, start-startPair)}")
        #y=input("enter a key: ")

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


locations=[]

for seed in seedPairs:
  correspond(seed, soilPairs, seedPairs, seed2SoilMap)
#print(f"seedPairs = {seedPairs}")
#y = input("enter a key: ")
#print(f"soilPairs = {soilPairs}")
#y = input("enter a key: ")

#[correspond(i) for i in j for j in bigLst]
# [seedPairs, soilPairs...]
for soil in soilPairs:
  correspond(soil, fertlPairs, soilPairs, soil2FertlMap)

for fertl in fertlPairs:
  correspond(fertl, waterPairs, fertlPairs, fertl2WaterMap)

for water in waterPairs:
  correspond(water, lightPairs, waterPairs, water2LightMap)

for light in lightPairs:
  correspond(light, tempPairs, lightPairs, light2TempMap)

for temp in tempPairs:
  correspond(temp, humidPairs, tempPairs, temp2HumidMap)

for humid in humidPairs:
  correspond(humid, locationPairs, humidPairs, humid2LocMap)

for loc in locationPairs:
  correspond(loc, locations, locationPairs, humid2LocMap)

print("before locations print")
print(locationPairs)
y = input("enter a key: ")
locations = list(map(tuple2starts, locationPairs))

print(min(locations))
print("end of code")