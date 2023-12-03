
def sortByValue (inDict):
  return sorted(inDict.items(), key=lambda x: x[1], reverse=False) #returns a tupple of str of digs and locs

def text2digit(sliceBF):
  textDigsDict={}
  textNumbers={"one": 1 , 
               "two": 2 , 
               "three": 3 , 
               "four": 4 , 
               "five": 5 , 
               "six": 6 , 
               "seven": 7 , 
               "eight": 8 , 
               "nine": 9 , 
               "zero": 0}
  for text in textNumbers:
    if text in sliceBF:
      textDigsDict[str(textNumbers[text])] = sliceBF.find(text) # {"one":18 // in mxmkjvgsdzfhseightonetwoeight}
  locs = list(textDigsDict.values())
  sortTextDigTupp = sortByValue(textDigsDict)
  
  return sortTextDigTupp[0][0], sortTextDigTupp[0][1]

def text2digitR(sliceAL):
  textDigsDict={}
  textNumbers={"one": 1 , 
               "two": 2 , 
               "three": 3 , 
               "four": 4 , 
               "five": 5 , 
               "six": 6 , 
               "seven": 7 , 
               "eight": 8 , 
               "nine": 9 , 
               "zero": 0}
  for text in textNumbers:
    if text in sliceBF:
      textDigsDict[str(textNumbers[text])] = sliceBF.find(text) # {"one":18 // in mxmkjvgsdzfhseightonetwoeight}
  locs = list(textDigsDict.values())
  sortTextDigTupp = sortByValue(textDigsDict)
  print(sortTextDigTupp)

  return sortTextDigTupp[-1][0], sortTextDigTupp[-1][1]

def findDigit(line):
  numbers = [str(i) for i in range (10)]
  for cha in line:
    if cha in numbers:
      return cha, line.index(cha)

      
f = open("day1_input.txt", "r")

digitsDict = {}
for line in f:
  line = line.strip()
  cha, indDigit = findDigit(line)
  digitsDict[cha] = indDigit
  sliceBF = line[:indDigit]
  print(f"line = {line}, cha = {cha}, indDigit = {indDigit}, sliceBF = {sliceBF}")
  
  text, indText = text2digit(sliceBF)
  print(f"text = {text}, indText = {indText}")
  digitsDict[text] = indText
  print(f"digitsDict = {digitsDict}")
  
  lineRL = [i for i in line]
  lineRL.reverse()
  lineRL = "".join(lineRL)
  cha, indDigit = findDigit(lineRL)
  if cha not in digitsDict:
    digitsDict[cha] = indDigit

  indDigit+=len(line)-1-indDigit
  print(indDigit)
  
  sliceAL = line[:indDigit] 
  print(f"sliceAL = {sliceAL}")
  
  text, indText = text2digitR(sliceAL)
  digitsDict[text] = indText
  print(text, indText)
  print(digitsDict)
  x = input("enter a key:")

  values = digitsDict.values()
  values.sort()
  print(f"first = {digitsDict.index(values[0])}, last = {digitsDict.index(values[-1])}")
  x = input("enter a key:")
f.close()




  
  
  