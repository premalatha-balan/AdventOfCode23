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
ends = np.array([node[2]=="Z" for node in node_starts])
#node_ends = [node for node in node_lst if node[2]=="Z"]
#print(f"starts = {node_starts} and len = {len(node_starts)} ")
#print(f"ends = {node_ends} and len = {len(node_ends)} ")
#y=input("enter a key: ")

step=0
prevLength=0
#move = lambda node, next: data[node][next]
length = len(instructions)
print(f"length = {length} ")
print(f"dir = {instructions[step]} entering in node = {node_starts} , len {len(instructions)} at step {step} ")
while True:
  length=len(instructions)
  i=instructions[step]
  if step==length-1 or step==prevLength+1 or step==prevLength: 
    print(f"entering at {step}, dir ={i} and node = {node_starts} and length = {length} ")
    y = input("enter a key: ")
  #print(f"dir = {i}entering in node = {node_starts} , len {len(instructions)} at step {step} ")
  #print(f"{node_starts} at the beginning")
  next = 0 if i=="L" else 1
  #move = lambda node: data[node][next]
  #node_starts = np.array([data[node][next] for node in node_starts])
  node_starts = list(map(lambda node: data[node][next], node_starts))
  step+=1
  #print(f"{node_starts} after {step} move")
  #y = input("enter a key: ")
  
  ends = np.array([node[2]=="Z" for node in node_starts])

  if any(ends):
    print(f"one of them have reached the path")
    print(f"at {step} node_starts {node_starts} ends {ends}")
    y = input("enter a key: ")
  if all(ends): break
  #print(f"ends = {ends} at step = {step} ")
  #y = input("enter a key: ")

  if step==length: 

    instructions=instructions + instructions
    prevLength = length
    length=len(instructions)
    print(f"repeating dir at {step}, dir ={i} and node = {node_starts} and length = {length} ")
    y = input("enter a key: ")
    #print(f"len = {len(instructions)} ")

print(step)