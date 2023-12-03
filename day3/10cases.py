
def findPartNumLoc(c):
  h0 = line.index(c)
  h00 = schema.index(line)
  hx=line.index(c)+1
  hy=schema.index(line)+1
  hx_=line.index(c)-1
  hy_=schema.index(line)-1
  return h0, h00, hx, hy, hx_, hy_


def goRight(line,x):
  count = x
  number = ""
  while line[count] in numbers and count<=len(line)-1:
    number+=line[count]
    count+=1
  return int(number) if number != "" else -1


def goLeft(line,x):
  count = x
  number = ""
  while line[count] in numbers and count>=0:
    number=line[count]+number
    count-=1
  return int(number) if number != "" else -1


def findNumX(c, hx): #adjacent right
  if hx<=len(line)-1:
    count = hx
    number = ""
    return goRight(line, hx)
  else:
    return -1


def findNumY(c, hy): #adjacent down going right
  if hy<=len(schema)-1:
    lineY = schema[hy]
    count = h0
    number = ""
    return goRight(lineY, h0)
  else:
    return -1


def findNumY_(c, hy_): #adjacent up going right
  if hy_>=0:
    lineY_ = schema[hy_]
    count = h0
    number = ""
    return goRight(lineY_, h0)
  else:
    return -1


def findNumX_(c, hx_): #adjacent left
  if hx_>=0:
    count = hx_
    number = ""
    return goLeft(line, hx_)
  else:
    return -1


def findNumX_Y(c, hy): #adjacent down going left
  if hy<=len(schema)-1:
    lineY = schema[hy]
    count = h0
    number = ""
    return goLeft(lineY, h0)
  else:
    return -1


def findNumX_Y_(c, hy_): #adjacent up going left
  if hy_>=0:
    lineY_ = schema[hy_]
    count = h0
    number = ""
    return goLeft(lineY_, h0)
  else:
    return -1


def findNumY(c, hy): #adjacent down diagonally & going right
  if hy<=len(schema)-1 and hx <=len(line)-1:
    lineY = schema[hy]
    count = hx
    number = ""
    return goRight(lineY, hx)
  else:
    return -1


def findNumY_(c, hy_): #adjacent up diagonally & going right
  if hy_>=0 and hx <=len(line)-1:
    lineY_ = schema[hy_]
    count = hx
    number = ""
    return goRight(lineY_, hx)
  else:
    return -1


 def findNumX_Y_(c, hy_): #adjacent up diagonally & going left
   if hy_>=0 and hx_>=0:
     lineY_ = schema[hy_]
     count = hx_
     number = ""
     return goLeft(lineY_, hx_)
   else:
     return -1


def findNumX_Y(c, hy): #adjacent down diagonally & going left
  if hy<=len(schema)-1 and hx_>=0:
    lineY = schema[hy]
    count = hx_
    number = ""
    return goLeft(lineY, hx_)
  else:
    return -1



f = open("day2_input.txt", "r")

schema = [line.strip() for line in f]

numbers = [str(i) for i in range(10)]

for line in schema:
  for c in line:
    if c!="." and c not in numbers:
      #print(f"found a symbol {c} in line {line} at {line.index(c)} in schema line {schema.index(line)} ")
      h0, h00, hx, hy, hx_, hy_ = findPartNumLoc(c)

      #print(f"h0 = {h0}, h00 = {h00}, hx = {hx}, hy = {hy}, hx_ = {hx_}, hy_ = {hy_}")

      #print(f"should be symbol = {schema[h00][h0]}")


      #y = input("enter a key: ")


f.close
