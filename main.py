
f=open("day5_input.txt", "r")

#reading 8 inputs
count = 0
for line in f:
  if count==0:
    #reading seeds info
    line = line.strip()
    seeds = (line[line.find(":")+1:]).strip().split()
    print(seeds)
    y = input("enter a key: ")

  elif count==1:
    #reading soilmap info
    line = line.strip()
    soilMap = (line[line.find(":")+1:]).strip().split()
    print(soi)
    y = input("enter a key: ")
  



f.close

