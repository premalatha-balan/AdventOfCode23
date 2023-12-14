import numpy as np
import copy
import math

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
travel = []
o_length = len(instructions)
for n in range(len(node_starts)):
  #initialising all things
  step = 0
  length = len(instructions)
  #print(f"length = {length}")
  node=node_starts[n]
  dir = instructions[0]
  next = 0 if dir == "L" else 1
  neighbour = data[node]
  #path=[(neighbour)]
  #nodesInPath = np.array(node)
  #print(path)
  #matches = {}
  while node[2]!="Z" and step<length:
    #print(f"inside the while loop with node {node}")
    #moving now
    next = 0 if dir =="L" else 1
    node = data[node][next] #this will give which node it should go next such as QKS for XSA (QKS, MND) and L 
    
    #this is to append everything
    step+=1
    neighbour = data[node]
  
    #decided to do the usual way as there is not a lot of gain in cutting the branches. maybe, but leaving it for now.
    dir = instructions[step]
    #path.append((neighbour))
    #nodesInPath = np.append(nodesInPath, (node))
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
  #print(step, n)
  #travel.append((node_starts[n], node, step))
  travel.append(step)
  #y = input("enter a key: ")
#print(f"length = {length}")
print(travel)

#travel.sort()
#print(travel)

result = int(math.prod(travel)/(o_length**5))
print(result)
print(5**2)


"""fw = open("path.txt", "w")
for tpl in path:
  tplStr = str(tpl)
  fw.write(tplStr)
  fw.write("\n")
fw.write(str(step+1))
fw.close"""
