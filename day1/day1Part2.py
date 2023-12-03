
def firstText (newLine):
  for i in textDigs:
    if i in newLine:
      return textDigs.index(i)
  return -1

def firstDig (newLine):
  for i in numbers:
    if i in newLine:
      return numbers.index(i)
  return -1 


f = open("day1_input.txt", "r")

textDigs = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

numbers = [str(i) for i in range(10)]

sumCalib = 0
count=0

for line in f:
  line = line.strip()
  newLine=""
  for c in line:
    newLine+=c
    fT = firstText(newLine)
    fD = firstDig(newLine)
    if fT!=-1 or fD!=-1:
      first = str(fT) if fT!=-1 else str(fD)
      #print(f"newLine = {newLine}")
      #print(f"first = {first}, fT = {fT}, fD = {fD} ")
      break
  newLine=""
  for i in range(len(line)-1, -1, -1):
    c = line[i]
    newLine = c+newLine
    lT = firstText(newLine)
    lD = firstDig(newLine)
    if lT!=-1 or lD!=-1:
      last = str(lT) if lT!=-1 else str(lD)
      #print(f"newLine = {newLine}")
      #print(f"last = {last}, lT = {lT}, lD = {lD} ")
      break
  output = int(first+last)
  sumCalib += output
  count+=1
  #print(f"line = {line}")
  #print(f"first = {first}, last = {last}, output = {output}")
  #print(f"sumCalib = {sumCalib}, count={count} ")
  #y = input("enter a key: \n")
  #print(f"line = {line} ")
  #print(f"first = {first}, last = {last}, output = {output}, sumCalib = {sumCalib}, count ={count} \n" )


print(sumCalib)

f.close()