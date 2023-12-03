
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
