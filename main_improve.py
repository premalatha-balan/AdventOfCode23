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

node_lst = list(data.keys())
#print(f"all nodes = {node_lst} ")
#node_starts = [node for node in node_lst if node[2]=="A"]
node_starts = np.array([node for node in node_lst if node[2] == "A"])
ends = np.array[node[2]=="Z" for node in node_starts]
#node_ends = [node for node in node_lst if node[2]=="Z"]
#print(f"starts = {node_starts} and len = {len(node_starts)} ")
#print(f"ends = {node_ends} and len = {len(node_ends)} ")
#y=input("enter a key: ")

step=0

#move = lambda node, next: data[node][next]
length = len(instructions)
while all.np(ends):
  i=instructions[step]
  #print(f"entering in node = {node} direction now = {i}, len {len(instructions)} ")
  #print(f"{node_starts} at the beginning")
  next = 0 if i=="L" else 1
  #move = lambda node: data[node][next]
  node_starts = np.array([data[node][next] for node in node_starts])
  #node_starts = list(map(lambda node: data[node][next], node_starts))
  #print(f"{node_starts} after move")
  step+=1
  ends = np.array[node[2]=="Z" for node in node_starts]
  #print(f"ends = {ends} at step = {step} ")
  #y = input("enter a key: ")

  if step==length-2: 
    #print(f"I am here at {step}, dir ={i} and node = {node} ")
    #y = input("enter a key: ")
    instructions=instructions*=2
    length=len(instructions)
    #print(f"len = {len(instructions)} ")
    
print(step)