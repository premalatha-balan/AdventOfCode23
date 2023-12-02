f = open("day1_input.txt", "r")

numbers = [str(i) for i in range(10)]
sumCalib=0
count=0

for line in f:
  for first in line:
    length = len(line)
    if first in numbers:
      #print(f"line ={line} first = {first} at {line.index(first)}")
      for last in range (length-1, -1, -1):
        if line[last] in numbers:
          #print(f"found {line[last]} at {last}")
          output = first+line[last]
          sumCalib+=int(output)
          print(f"output = {output}, sum = {sumCalib}, count = {count} ")
          break
      break
  