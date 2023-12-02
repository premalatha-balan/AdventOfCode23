#Advent of Code
# Day 1

def findDigit(data):
  numbers = {}
  for i in range(10):
    found = data.find(str(i))
    #print(f"{found}, i = {i}, data = {data[i]} ")
    if found != -1:
      numbers[found] = i
  return numbers

def getOutput(numbers):
  if len(numbers) == 1:
    myKeys = list(numbers.keys())
    output = str(numbers[myKeys[0]]) + str(numbers[myKeys[0]])
    #print(f"{output}")
  elif len(numbers) >= 2:
    myKeys = list(numbers.keys())
    myKeys.sort()
    numbers = {i: numbers[i] for i in myKeys}
    output = str(numbers[myKeys[0]]) + str(numbers[myKeys[-1]])
    #print(f"{output}")
  else:
    print("there are no digits in this line")
    output = "-1"
  return output

f = open("day1_input.txt", "r")
for i in range(5):
  data = f.readline()
  numbers = findDigit(data)
  output = getOutput(numbers)
  print(f"{output}")
  print(f"{numbers}")
  print(f"{data}")

f.close()
