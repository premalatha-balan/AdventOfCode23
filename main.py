
def findPartNumLoc(c):
  h0 = line.index(c)
  h00 = schema.index(line)
  hx=line.index(c)+1
  hy=schema.index(line)+1
  hx_=line.index(c)-1
  hy_=schema.index(line)-1
  return h0, h00, hx, hy, hx_, hy_

def findNumX(c, hx):
  if line[hx] in numbers:
    count = hx
    number = ""
    while line[count] in numbers or count<=len(line)-1:
      number+=line[count]
      count+=1
    return int(number)
  else:
    return -1


def findNumY(c, hy):
  lineY = schema[hy]
  if lineY[h0] in numbers:
    count = h0
    number = ""
    while lineY[count] in numbers or count<=len(lineY)-1:
      number+=lineY[count]
      count+=1
    return int(number)
  else:
    return -1


def findNumY_(c, hy_):
  lineY_ = schema[hy_]
  if lineY_[h0] in numbers:
    count = h0
    number = ""
    while lineY_[count] in numbers or count<=len(lineY_)-1:
      number+=lineY_[count]
      count+=1
    return int(number)
  else:
    return -1


def findNumX_(c, hx_):
  if line[hx_] in numbers:
    count = hx_
    number = ""
    while line[count] in numbers or count>=0:
      number=line[count]+number
      count-=1
    return int(number)
  else:
    return -1

def findNumX_(c, hx_):
  if line[hx_] in numbers:
    count = hx_
    number = ""
    while line[count] in numbers or count>=0:
      number=line[count]+number
      count-=1
    return int(number)
  else:
    return -1


f = open("day2_input.txt", "r")

schema = [line.strip() for line in f]

numbers = [str(i) for i in range(10)]

for line in schema:
  for c in line:
    if c!="." and c not in numbers:
      print(f"found a symbol {c} in line {line} at {line.index(c)} in schema line {schema.index(line)} ")
      h0, h00, hx, hy, hx_, hy_ = findPartNumLoc(c)
      print(f"h0 = {h0}, h00 = {h00}, hx = {hx}, hy = {hy}, hx_ = {hx_}, hy_ = {hy_}")
      
      print(f"should be symbol = {schema[h00][h0]}")

      
      y = input("enter a key: ")
      

f.close
