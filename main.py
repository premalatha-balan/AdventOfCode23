
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
    #print(f"line {line}")
    #y = input("enter a key at line")
    while len(line)>0:
      #print(f"line {line}, length {len(line)}, count = {count} ")
      #y = input("enter a key at while loop")
      #reading soilmap info
      line = str(f.readlines(1))
     # print(f"line {line} inside while loop")
      line = line.strip("[]\n'")
      #print(f"stripped line {line}")
      addline2soil = (line[line.find(":")+1:-2]).strip().split()
      #print(f"addline2soil {addline2soil} length = {len(addline2soil)} ")
      if len(addline2soil)<=0:break
      #print(f"addline2soil {addline2soil}")
      soilMap.append(addline2soil)
      print(soilMap)
      #y = input("enter a key at soil: ")
  elif count==3:
    fertlMap=[]
    #print(f"line {line}")
    #y =input("enter a ke#y at line")
    line = line.strip("[]\n'")
    addline2fert = (line[line.find(":")+1:]).strip().split()
    #print(f"addline2fert {addline2fert} length = {len(addline2fert)} ")
    if len(addline2fert)<=0:break
    #print(f"addline2fert {addline2fert}")
    fertlMap.append(addline2fert)
    #print(fertlMap) 
    #y =input("enter a key at fertMap first line")
    while len(line)>0:
      #print(f"line {line}, length {len(line)}, count = {count} ")
      #y = input("enter a key inside fert while loop")
      #reading soilmap info
      line = str(f.readlines(1))
      # print(f"line {line} inside while loop")
      line = line.strip("[]\n'")
      #print(f"stripped line {line}")
      addline2fert = (line[line.find(":")+1:-2]).strip().split()
      #print(f"addline2fert {addline2fert} length = {len(addline2fert)} ")
      if len(addline2fert)<=0:break
      #print(f"addline2fert {addline2fert}")
      fertlMap.append(addline2fert)
      #print(fertlMap)
      #y = input("enter a key at fert end of while loop: ")
  elif count==4:
    waterMap=[]
    #print(f"line {line}")
    y =input("enter a key at line")
    line = line.strip("[]\n'")
    addline2water = (line[line.find(":")+1:]).strip().split()
    #print(f"addline2water {addline2water} length = {len(addline2water)} ")
    if len(addline2water)<=0:break
    #print(f"addline2water {addline2water}")
    waterMap.append(addline2water)
    #print(waterMap) 
    #y =input("enter a key at waterMap first line")
    while len(line)>0:
      #print(f"line {line}, length {len(line)}, count = {count} ")
      #y = input("enter a key inside water while loop")
      #reading soilmap info
      line = str(f.readlines(1))
      # #print(f"line {line} inside while loop")
      line = line.strip("[]\n'")
      #print(f"stripped line {line}")
      addline2water = (line[line.find(":")+1:-2]).strip().split()
      #print(f"addline2water {addline2water} length = {len(addline2water)} ")
      if len(addline2water)<=0:break
      #print(f"addline2water {addline2water}")
      waterMap.append(addline2water)
      #print(waterMap)
      #y = input("enter a key at water end of while loop: ")
  elif count==5:
    lightMap=[]
    #print(f"line {line}")
    #y =input("enter a ke#y at line")
    line = line.strip("[]\n'")
    addline2light = (line[line.find(":")+1:]).strip().split()
    #print(f"addline2light {addline2light} length = {len(addline2light)} ")
    if len(addline2light)<=0:break
    #print(f"addline2light {addline2light}")
    lightMap.append(addline2light)
    #print(lightMap) 
    #y =input("enter a key at lightMap first line")
    while len(line)>0:
      #print(f"line {line}, length {len(line)}, count = {count} ")
      #y = input("enter a key inside light while loop")
      #reading soilmap info
      line = str(f.readlines(1))
      # print(f"line {line} inside while loop")
      line = line.strip("[]\n'")
      #print(f"stripped line {line}")
      addline2light = (line[line.find(":")+1:-2]).strip().split()
      #print(f"addline2light {addline2light} length = {len(addline2light)} ")
      if len(addline2light)<=0:break
      #print(f"addline2light {addline2light}")
      lightMap.append(addline2light)
      #print(lightMap)
      #y = input("enter a key at light end of while loop: ")
  elif count==6:
    tempMap=[]
    #print(f"line {line}")
    #y =input("enter a key at line")
    line = line.strip("[]\n'")
    addline2temp = (line[line.find(":")+1:]).strip().split()
    #print(f"addline2temp {addline2temp} length = {len(addline2temp)} ")
    if len(addline2temp)<=0:break
    #print(f"addline2temp {addline2temp}")
    tempMap.append(addline2temp)
    #print(tempMap) 
    #y =input("enter a key at tempMap first line")
    while len(line)>0:
      #print(f"line {line}, length {len(line)}, count = {count} ")
      #y = input("enter a key inside temp while loop")
      #reading soilmap info
      line = str(f.readlines(1))
      # #print(f"line {line} inside while loop")
      line = line.strip("[]\n'")
      ##print(f"stripped line {line}")
      addline2temp = (line[line.find(":")+1:-2]).strip().split()
      #print(f"addline2temp {addline2temp} length = {len(addline2temp)} ")
      if len(addline2temp)<=0:break
      #print(f"addline2temp {addline2temp}")
      tempMap.append(addline2temp)
      #print(tempMap)
      #y = input("enter a key at temp end of while loop: ")
  elif count==7:
    humidMap=[]
    #print(f"line {line}")
    #y =input("enter a key at line")
    line = line.strip("[]\n'")
    addline2humid = (line[line.find(":")+1:]).strip().split()
    #print(f"addline2humid {addline2humid} length = {len(addline2humid)} ")
    if len(addline2humid)<=0:break
    #print(f"addline2humid {addline2humid}")
    humidMap.append(addline2humid)
    #print(humidMap) 
    #y =input("enter a key at humidMap first line")
    while len(line)>0:
      #print(f"line {line}, length {len(line)}, count = {count} ")
      #y = input("enter a key inside humid while loop")
      #reading soilmap info
      line = str(f.readlines(1))
      # #print(f"line {line} inside while loop")
      line = line.strip("[]\n'")
      ##print(f"stripped line {line}")
      addline2humid = (line[line.find(":")+1:-2]).strip().split()
      #print(f"addline2humid {addline2humid} length = {len(addline2humid)} ")
      if len(addline2humid)<=0:break
      #print(f"addline2humid {addline2humid}")
      humidMap.append(addline2humid)
      #print(humidMap)
      #y = input("enter a key at humid end of while loop: ")
  elif count==8:
    locMap=[]
    #print(f"line {line}")
    #y =input("enter a key at line")
    line = line.strip("[]\n'")
    addline2loc = (line[line.find(":")+1:]).strip().split()
    #print(f"addline2loc {addline2loc} length = {len(addline2loc)} ")
    if len(addline2loc)<=0:break
    #print(f"addline2loc {addline2loc}")
    locMap.append(addline2loc)
    #print(locMap) 
    #y =input("enter a key at locMap first line")
    while len(line)>0:
      #print(f"line {line}, length {len(line)}, count = {count} ")
      #y = input("enter a key inside loc while loop")
      #reading soilmap info
      line = str(f.readlines(1))
      # #print(f"line {line} inside while loop")
      line = line.strip("[]\n'")
      ##print(f"stripped line {line}")
      addline2loc = (line[line.find(":")+1:-2]).strip().split()
      #print(f"addline2loc {addline2loc} length = {len(addline2loc)} ")
      if len(addline2loc)<=0:break
      #print(f"addline2loc {addline2loc}")
      locMap.append(addline2loc)
      #print(locMap)
      #y = input("enter a key at loc end of while loop: ")
  count+=1

print(f"left the for loop too. ")
f.close

