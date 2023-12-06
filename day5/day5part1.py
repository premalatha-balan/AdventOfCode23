
def readFile2Data():
  f=open("day5_input.txt", "r")
  
  #reading the file and storing it in a list
  inData = [line.strip() for line in f if (line != "" and line != " " and line != "\n")]
  #print(inData)
  
  seeds = inData[0].split()
  seeds.remove("seeds:")
  seeds = [int(i) for i in seeds]
  
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
  return(seeds, seed2SoilMap, soil2FertlMap, fertl2WaterMap, water2LightMap, light2TempMap, temp2HumidMap,humid2LocMap)

x = lambda a, b, start, end: a if a<start or a>end else b+(a-start)

def checkRange(mapElement, mapData):
  #The range is start+range-1
  #print(f"len = {len(mapData)}")
  for line in mapData:
    start, end = line[1], line[1]+line[2]-1 
    
    match=x(mapElement, line[0], start, end)

    if match!=mapElement: return match
       
  return(match)



#main 
seeds, seed2SoilMap, soil2FertlMap, fertl2WaterMap, water2LightMap, light2TempMap, temp2HumidMap, humid2LocMap =  readFile2Data()

locations=[]
correspond=[]
for seed in seeds:
  corres=[]
  corres.append(seed)
  s2SMatch = checkRange(seed, seed2SoilMap)
  corres.append(s2SMatch)
  #print(f"s2SMatch = {s2SMatch}")
  s2FMatch = checkRange(s2SMatch, soil2FertlMap)
  corres.append(s2FMatch)
  #print(f"s2FMatch = {s2FMatch}")
  f2WMatch = checkRange(s2FMatch, fertl2WaterMap)
  corres.append(f2WMatch)
  #print(f"f2WMatch = {f2WMatch}")
  w2LMatch = checkRange(f2WMatch, water2LightMap)
  corres.append(w2LMatch)
  #print(f"w2LMatch = {w2LMatch}")
  l2TMatch = checkRange(w2LMatch, light2TempMap)
  corres.append(l2TMatch)
  #print(f"l2TMatch = {l2TMatch}")
  t2HMatch = checkRange(l2TMatch, temp2HumidMap)
  corres.append(t2HMatch)
  #print(f"t2HMatch = {t2HMatch}")
  h2LMatch = checkRange(t2HMatch, humid2LocMap)
  locations.append(h2LMatch)
  corres.append(h2LMatch)
  correspond.append(corres)
  #print(f"h2LMatch = {h2LMatch}")
  #print(f"for seed {seed} s2SMatch = {s2SMatch}, s2FMatch = {s2FMatch}, f2WMatch = {f2WMatch}, w2LMatch = {w2LMatch}, l2TMatch = {l2TMatch}, t2HMatch = {t2HMatch}, h2LMatch = {h2LMatch}" )
  #print(f"Location = {h2LMatch}")
  #y=input("enter a key: ")

#print(locations)
#print(min(locations))
print(correspond)
print(min(locations))