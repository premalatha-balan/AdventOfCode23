
def findPartNumLoc(c):
  hx = line.index(c)+1
  hx_ = line.index(c)-1
  hy = schema.index(line)+1
  hy_ = schema.index(line)-1
  return (hx, hy, hx_, hy_)


f = open("day2_input.txt", "r")

schema = [line.strip() for line in f]

numbers = [str(i) for i in range(10)]

for line in schema:
  for c in line:
    if c!="." and c not in numbers:
      print(f"found a symbol {c} in line {line} ")
      hx,hy,hx_,hy_ = findPartNumLoc(c)
      y = input("enter a key: ")

f.close
