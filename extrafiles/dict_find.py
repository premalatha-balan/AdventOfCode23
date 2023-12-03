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

sumCalib = 0
count=0
for data in f:
  #data = f.readline()
  numbers = findDigit(data)
  output = getOutput(numbers)
  sumCalib+=int(output)
  count+=1
  print(f"output = {output}, count = {count}, sum = {sumCalib}")
  print(f"numbers = {numbers}, ")
  print(f"{data}")
  #x = input("enter a key: ")

f.close()
print(f"The sum of all output values is {sumCalib}")
