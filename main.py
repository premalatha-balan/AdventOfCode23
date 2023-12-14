import numpy as np

def readFile2Data():
  f=open("day8_input.txt", "r")

  data = [line.strip() for line in f]
  instructions = data[0]

  data.pop(0)
  data.pop(0)

  data = [line.split(" ") for line in data]
  data = {line[0] : (line[2].strip("(,"), line[3].strip(")")) for line in data}

  f.close
  return(instructions, data)

instructions, data = readFile2Data()
instr_loc_tpl = list(enumerate(instructions))
"""fi = open("instructions.txt", "w")
for i in instr_loc_tpl:
  tplStr = str(i)
  fi.write(tplStr)
  fi.write("\n")
fi.close()"""
node_lst = list(data.keys())
#neighbours_lst = list(data.values())
node_starts = np.array([node for node in node_lst if node[2] == "A"])
print(node_starts)
#print(neighbours_lst)
#y = input("enter a key")

#initialising all things
step = 0
length = len(instructions)
node=node_starts[0]
dir = instructions[0]
next = 0 if dir == "L" else 1
neighbour = data[node]
path=[(neighbour)]
nodesInPath = np.array(node)
#print(path)
matches = {}
while node[2]!="Z" and step<length:
  #print(f"inside the while loop with node {node}")
  #moving now
  next = 0 if dir =="L" else 1
  node = data[node][next] #this will give which node it should go next such as QKS for XSA (QKS, MND) and L 
  
  #this is to append everything
  step+=1
  neighbour = data[node]

  if neighbour in path:
    #print(f"neighbour {neighbour} is in path {path} ")
    #y = input("enter a key: ")
    if neighbour not in matches:
      initial = path.index(neighbour)
      matches.update({neighbour:[initial, step]}) 
      dir_now = instructions[initial:step]
      #making sure the length of the instructions is enough
      if length<step*2-initial:
        instructions=instructions*2
        length = len(instructions)
      #checking out if there is branch in the  previously matched ones which we can take and add to the path
      for i in range(1,len(dir_now)):
        l = dir_now[i]
        r = instructions[step+1]
        if l == r:
          print(f"checking out at {i} and {step+1}")
          #this is worth cutting a branch and adding it although only two here. Prefer to do more than two.
          y = input("enter a key: ")
        else:
          print(f"don't bother at {i} and {step+1}")
          y = input("enter a key: ")
                
        
      #working here
    else:
      print(f"Yes, there are more than one matches at {neighbour} at {step} ")
      matches[neighbour].append(step)
    print(matches)
    y = input("enter a key: ")
  
  dir = instructions[step]
  path.append((neighbour))
  nodesInPath = np.append(nodesInPath, (node))
  #print(f"path = {path}")
  #print(f"step = {step} ")
  #print(f"node = {node}")
  #y = input("enter a key: ")

  if step == length-1:
    #print(f"inside if checking length {length} ")
    instructions=instructions*2
    length=len(instructions)
    #print(f"length = {length}")
    #y = input("enter a key: ")

#print(path)
#print(step+1)

"""fw = open("path.txt", "w")
for tpl in path:
  tplStr = str(tpl)
  fw.write(tplStr)
  fw.write("\n")
fw.write(str(step+1))
fw.close"""
