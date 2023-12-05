
f=open("day5_input.txt", "r")

#reading 8 inputs
count = 0
for line in f:
  if count==0:
    #reading seeds info
    line = line.strip()
    seeds = (line[line.find(":")+1:]).strip().split()
    #line=[1,2,3] #making line not empty at the end of reading seeds
    print(seeds)
    #y = input("enter a key at seeds: ")

  elif count==2:
    soilMap=[]
    print(f"line {line}")
    y = input("enter a key at line")
    while len(line)>0:
      print(f"line {line}, length {len(line)}")
      y = input("enter a key at while loop")
      #reading soilmap info
      line = str(f.readlines(1))
      print(f"line {line}")
      line = line.strip("[]\n'")
      print(f"stripped line {line}")
      soilMap.append((line[line.find(":")+1:-2]).strip().split())
      print(soilMap)
      #y = input("enter a key at soil: ")
  elif count==4:
    print(f"I am in count {count}")
    y = input("enter a key at fert: ")
  

  count+=1

f.close

