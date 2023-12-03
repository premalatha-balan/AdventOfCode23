
def findPartNumLoc(c):
  x0 = line.index(c)
  y0 = schema.index(line)
  hx=line.index(c)+1
  hy=schema.index(line)+1
  hx_=line.index(c)-1
  hy_=schema.index(line)-1
  return x0, y0, hx, hy, hx_, hy_


def goRight(line,x,number):
  count = x
  while line[count] in numbers and count<=len(line)-1:
    number+=line[count]
    count+=1
  return int(number) if number != "" else -1


def goLeft(line,x, number):
  count = x
  while line[count] in numbers and count>=0:
    number=line[count]+number
    count-=1
  return int(number) if number != "" else -1


def caseX(c, hx): #adjacent right
  if hx<=len(line)-1:
    number = ""
    return goRight(line, hx, number) 
  else:
    return -1


def caseX_(c, hx_): #adjacent left
  if hx_>=0:
    number = ""
    return goLeft(line, hx_,number)
  else:
    return -1


def caseYX(c, hy): #adjacent down diagonally & going right
  if hy<=len(schema)-1 and hx <=len(line)-1:
    lineY = schema[hy]
    if lineY[x0] in numbers: return -1
    number = ""
    return goRight(lineY, hx, number)
  else:
    return -1


def caseYX_(c, hy): #adjacent down diagonally & going left
  if hy<=len(schema)-1 and hx_>=0:
    lineY = schema[hy]
    if lineY[x0] in numbers: return -1
    number = ""
    return goLeft(lineY, hx_,number)
  else:
    return -1


def caseY_X(c, hy_): #adjacent up diagonally & going right
  if hy_>=0 and hx <=len(line)-1:
    lineY_ = schema[hy_]
    if lineY_[x0] in numbers: return -1
    number = ""
    return goRight(lineY_, hx, number)
  else:
    return -1


def fcaseY_X_(c, hy_): #adjacent up diagonally & going left
  if hy_>=0 and hx_>=0:
   lineY_ = schema[hy_]
   if lineY_[x0] in numbers: return -1
   number = ""
   return goLeft(lineY_, hx_,number)
  else:
   return -1


def caseYX_X(c, hy): #adjacent down starting a bit to the left & going right
  if hy<=len(schema)-1 and hx_>=0:
    lineY = schema[hy]
    number = ""
    number = str(goLeft(lineY, x0,number)) if goLeft(lineY, x0,number) != -1 else number
    number = number.rstrip(number[-1]) if number !="" else number
    number = str(goRight(lineY, x0,number))
    return int(number)
  else:
    return -1


def caseY_X_X(c, hy_): #adjacent up starting a bit to the left & going right
  if hy_>=0 and hx_>=0:
    lineY_ = schema[hy_] 
    number = ""
    number = str(goLeft(lineY_, x0,number)) if goLeft(lineY_, x0,number) != -1 else number
    number = number.rstrip(number[-1]) if number !="" else number
    number = str(goRight(lineY_, x0,number))
    return int(number)
  else:
    return -1


f = open("day2_input.txt", "r")

schema = [line.strip() for line in f]

numbers = [str(i) for i in range(10)]
atIndex = -1
sumPartNumbers = 0
for line in schema:
  for i in range(len(line)):
    c=line[i]
    if c!="." and c not in numbers:
      print(f"c = {c} at the beginning")
      #print(f"found a symbol {c} in line {line} at {line.index(c)} in schema line {schema.index(line)} ")
      x0, y0, hx, hy, hx_, hy_ = findPartNumLoc(c)
      numberI = 0
      numberI = caseX(c, hx) if caseX(c, hx) != -1 else 0 #adjacent right
      sumPartNumbers += numberI 
      print(f"sum = {sumPartNumbers} and numberI = {numberI} right") 
      numberI = caseX_(c, hx_) if caseX_(c, hx_) != -1 else 0 #adjacent left
      sumPartNumbers += numberI 
      print(f"sum = {sumPartNumbers} and numberI = {numberI} left") 
      numberI = caseYX(c, hy) if caseYX(c, hy) != -1 else 0 #adjacent down diagonally & going right
      sumPartNumbers += numberI 
      print(f"sum = {sumPartNumbers} and numberI = {numberI} diag down right")
      numberI = caseYX_(c, hy) if caseYX_(c, hy) != -1 else 0 #adjacent down diagonally & going left
      sumPartNumbers += numberI 
      print(f"sum = {sumPartNumbers} and numberI = {numberI} diag down left")
      numberI = caseY_X(c, hy_) if caseY_X(c, hy_) != -1 else 0 #adjacent up diagonally & going right
      sumPartNumbers += numberI 
      print(f"sum = {sumPartNumbers} and numberI = {numberI} diag up right")
      numberI = fcaseY_X_(c, hy_) if fcaseY_X_(c, hy_) != -1 else 0 #adjacent up diagonally & going left
      sumPartNumbers += numberI 
      print(f"sum = {sumPartNumbers} and numberI = {numberI} diag up left")
      numberI = caseYX_X(c, hy) if caseYX_X(c, hy) != -1 else 0 #adjacent down starting a bit to the left & going right
      sumPartNumbers += numberI 
      print(f"sum = {sumPartNumbers} and numberI = {numberI} down and a bit")
      numberI = caseY_X_X(c, hy_) if caseY_X_X(c, hy_) != -1 else 0 #adjacent up starting a bit to the left & going right
      sumPartNumbers += numberI 
      print(f"sum = {sumPartNumbers} and numberI = {numberI} up a bit")

      print(f"sum = {sumPartNumbers} at symbol {c} at {line.index(c)} in schema line {schema.index(line)} ")

      atIndex = line.index(c)
 
      
      #print(f"x0 = {x0}, y0 = {y0}, hx = {hx}, hy = {hy}, hx_ = {hx_}, hy_ = {hy_}")
      
      #print(f"should be symbol = {schema[y0][x0]}")

      
      y = input("enter a key: ")
print(sumPartNumbers)

f.close
