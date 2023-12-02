import copy

def text2num(line):
  textNumbers = ["zero",
                 "one",
                "two",
                "three",
                "four",
                "five",
                "six",
                "seven",
                "eight",
                "nine"
                ]
  numbers = [str(i) for i in range(10)]
  print(f"line = {line} ")
  line2=[]
  for i in range(10):
    if line.find(textNumbers[i]) != -1:
      line2.append(str(i))
  print(f"line2 = {line2}")
  return line2


f = open("day1_input.txt", "r")

numbers = [str(i) for i in range(10)]
sumCalib=0
count=0
for line in f:
  for first in line2:
    length = len(line2)
    if first in numbers:
      sliceF = line[0:line.index(first)]
      lineSF = text2num(sliceF)
      #print(f"line ={line} first = {first} at {line.index(first)}")
      for last in range (length-1, -1, -1):
        if line2[last] in numbers:
          #print(f"found {line[last]} at {last}")
          output = first+line2[last]
          sumCalib+=int(output)
          #print(f"output = {output}, sum = {sumCalib}, count = {count} ")
          break
      break




