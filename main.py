
def readFile2Data()
  f=open("day5_input.txt", "r")
  
  #reading the file and storing it in a list
  inData = [line.strip() for line in f if (line != "" and line != " " and line != "\n")]
  #print(inData)
  
  seeds = inData[0].split()
  seeds.remove("seeds:")
  
  soilMap = inData[2:inData.index("soil-to-fertilizer map:")]
  soilMap = [line.split() for line in soilMap]
  #print(soilMap)
  
  fertlMap = inData[inData.index("soil-to-fertilizer map:")+1:inData.index("fertilizer-to-water map:")]
  fertlMap = [line.split() for line in fertlMap]
  #print(fertlMap)
  
  waterMap = inData[inData.index("fertilizer-to-water map:")+1:inData.index("water-to-light map:")]
  waterMap = [line.split() for line in waterMap]
  #print(f"waterMap = {waterMap}")
  
  lightmap  = inData[inData.index("water-to-light map:")+1:inData.index("light-to-temperature map:")]
  lightmap = [line.split() for line in lightmap]
  #print(f"lightmap = {lightmap}")
  
  tempMap = inData[inData.index("light-to-temperature map:")+1:inData.index("temperature-to-humidity map:")]
  tempMap = [line.split() for line in tempMap]
  #print(f"tempMap = {tempMap}")
  
  humidMap = inData[inData.index("temperature-to-humidity map:")+1:inData.index("humidity-to-location map:")]
  humidMap = [line.split() for line in humidMap]
  #print(f"humidMap = {humidMap}")
  
  locMap = inData[inData.index("humidity-to-location map:")+1:]
  locMap = [line.split() for line in locMap]
  print(f"locMap = {locMap}")
  
  print(f"left the for loop too. ")
  f.close
  return(seeds, soilMap, fertlMap, waterMap, lightmap, tempMap, humidMap,)

readFile2Data()


