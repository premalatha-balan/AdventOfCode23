
def findPartNumLoc(c):
  x0 = j
  y0 = i
  hx=j+1
  hy=i+1
  hx_=j-1
  hy_=i-1
  return x0, y0, hx, hy, hx_, hy_


def goRight(line,x):
  count = x
  number=""
  while count<=len(line)-1 and line[count] in numbers :
    number= number+line[count]
    count+=1
  return int(number) if number != "" else -1


def goLeft(line,x):
  count = x
  number = ""
  while count>=0 and line[count] in numbers:
    number=line[count]+number
    count-=1
  return int(number) if number != "" else -1


def goLeft_Right(lineF,x):
  if lineF[x] not in numbers or x<0: return -1
  number=""
  count = x
  while count>=0 and lineF[count] in numbers:
    #print(f"lineF{count} = {lineF[count]}")
    count-=1
  #print(f"count = {count}, started at {x}")
  count+=1
  if count>=0:
    #print("I am in")
    #print(f"first check {count}<= {len(lineF)-1} and second check {lineF[count]}")
    while count<=len(lineF)-1 and lineF[count] in numbers:
      #print("I am in too")
      number= number+lineF[count]
      #print(f"number = {number} at count = {count} ")
      count+=1
    return int(number) if number != "" else -1
  else:
    return -1


def caseX(c, hx): #adjacent right
  if hx<=len(line)-1:
    return goRight(line, hx) 
  else:
    return -1


def caseX_(c, hx_): #adjacent left
  if hx_>=0:
    return goLeft(line, hx_)
  else:
    return -1


def caseYX(c, hy): #adjacent down diagonally & going right
  if hy<=len(schema)-1 and hx <=len(line)-1:
    lineY = schema[hy]
    if lineY[x0] in numbers: return -1
    return goRight(lineY, hx)
  else:
    return -1


def caseYX_(c, hy): #adjacent down diagonally & going left
  if hy<=len(schema)-1 and hx_>=0:
    lineY = schema[hy]
    if lineY[x0] in numbers: return -1
    return goLeft(lineY, hx_)
  else:
    return -1


def caseY_X(c, hy_): #adjacent up diagonally & going right
  if hy_>=0 and hx <=len(line)-1:
    lineY_ = schema[hy_]
    if lineY_[x0] in numbers: return -1
    return goRight(lineY_, hx)
  else:
    return -1


def fcaseY_X_(c, hy_): #adjacent up diagonally & going left
  if hy_>=0 and hx_>=0:
   lineY_ = schema[hy_]
   if lineY_[x0] in numbers: return -1
   return goLeft(lineY_, hx_)
  else:
   return -1


def caseYX_X(c, hy): #adjacent down starting a bit to the left & going right
  if hy<=len(schema)-1 and hx_>=0:
    lineY = schema[hy]
    return goLeft_Right(lineY,x0)
  else:
    return -1


def caseY_X_X(c, hy_): #adjacent up starting a bit to the left & going right
  if hy_>=0 and hx_>=0:
    lineY_ = schema[hy_] 
    return goLeft_Right(lineY_,x0)
  else:
    return -1


f = open("day3_input.txt", "r")

schema = [line.strip() for line in f]

numbers = [str(i) for i in range(10)]
#atIndex = -1

#sumPartNumbers = 0
sumGears = 1
for i in range(len(schema)):
  line = schema[i]
  for j in range(len(line)):
    c=line[j]
    #if atIndex == line.index(c): continue
    #print(f"c at {j}: {c}" )
    if c=="*":
      #print(f"c = {c} at the beginning")
      #print(f"found a symbol {c} at {j} in schema line {i} ")
      x0, y0, hx, hy, hx_, hy_ = findPartNumLoc(c)
      numberI = 0
      adjNums = []
      numberI = caseX(c, hx) if caseX(c, hx) != -1 else 0 #adjacent right
      adjNums.append(numberI) 
      #print(f"sum = {sumPartNumbers} and numberI = {numberI} right") 
      numberI = caseX_(c, hx_) if caseX_(c, hx_) != -1 else 0 #adjacent left
      adjNums.append(numberI)  
      #print(f"sum = {sumPartNumbers} and numberI = {numberI} left") 
      numberI = caseYX(c, hy) if caseYX(c, hy) != -1 else 0 #adjacent down diagonally & going right
      adjNums.append(numberI)  
      #print(f"sum = {sumPartNumbers} and numberI = {numberI} diag down right")
      numberI = caseYX_(c, hy) if caseYX_(c, hy) != -1 else 0 #adjacent down diagonally & going left
      adjNums.append(numberI) 
      #print(f"sum = {sumPartNumbers} and numberI = {numberI} diag down left")
      numberI = caseY_X(c, hy_) if caseY_X(c, hy_) != -1 else 0 #adjacent up diagonally & going right
      adjNums.append(numberI)  
      #print(f"sum = {sumPartNumbers} and numberI = {numberI} diag up right")
      numberI = fcaseY_X_(c, hy_) if fcaseY_X_(c, hy_) != -1 else 0 #adjacent up diagonally & going left
      adjNums.append(numberI)  
      #print(f"sum = {sumPartNumbers} and numberI = {numberI} diag up left")
      numberI = caseYX_X(c, hy) if caseYX_X(c, hy) != -1 else 0 #adjacent down starting a bit to the left & going right
      adjNums.append(numberI)  
      #print(f"sum = {sumPartNumbers} and numberI = {numberI} down and a bit")
      numberI = caseY_X_X(c, hy_) if caseY_X_X(c, hy_) != -1 else 0 #adjacent up starting a bit to the left & going right
      adjNums.append(numberI)  
      #print(f"sum = {sumPartNumbers} and numberI = {numberI} up a bit")

      #print(f"sum = {sumPartNumbers} at symbol {c} at {line.index(c)} in schema line {schema.index(line)} ")

      #atIndex = line.index(c)
      #c="."
 
      
      #print(f"x0 = {x0}, y0 = {y0}, hx = {hx}, hy = {hy}, hx_ = {hx_}, hy_ = {hy_}")
      
      #print(f"should be symbol = {schema[y0][x0]}")

      
      #y = input("enter a key: ")
  
      if len(adjNums)>=2:
        #print(f"at line {i} and loc {j} and adjNums = {adjNums}")
        numCount = 0
        ratioGears = 1
        for nums in adjNums:
          if nums != 0: 
            numCount += 1
            ratioGears*=nums
        if numCount>2: 
          #print(f"at line {i} and loc {j} and adjNums = {adjNums}")
          #print(f"num of adjs = {numCount}") 
          #y = input("enter a key: ")
          print("there were too many gears")
        #y = input("enter a key: ")
      else:
        print(f"at line {i} and loc {j} and adjNums = {adjNums}")
        #y = input("enter a key: ")
        
        
#print(sumPartNumbers)

f.close
