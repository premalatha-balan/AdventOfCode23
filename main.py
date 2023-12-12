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
neighbours_lst = list(data.values())
node_starts = np.array([node for node in node_lst if node[2] == "A"])
print(node_starts)

#ends = np.array[node for node in node_lst if node[2] == "Z"]

def move(node, next):
  return data[node][next] # do I need this? I will use map and lambda

step = 0
path=[]
length = len(instructions)
node=node_starts[0]
matches = []
while True:
  i = instructions[step]
  next = 0 if i == "L" else 1
  neighbour = data[node]
  #print(f"node = {node}, next = {next}, neighbour = {neighbour}" )
  #y = input("enter a key: ")
  node = data[node][next]
  next_path = (neighbour, i)
  #print(next_path)
  if next_path in path:
    print(f"at {step}, dir ={i} and node = {node}, next_path = {next_path}")
    path_now_lst = list(enumerate(path))
    
    #matches = [matches+ [posn] for posn in positions]
    #matches.append(positions)

    print(f"positions = {positions}")
    print(f"len = {len(positions)}")
    if len(positions) > 1: print("we have more than one position")
      for posn in positions:
        matches.append(posn)
        print(f"paths = {path[posn]} and path = {path[posn+1]}")
    
    else: 
    if len(matches)>1:
      dir_first = instructions[matches[0]:matches[1]]
      dir_next = instructions[step:matches[1]]
    #dir_now = instructions[:step]
    #dir_next = instructions[61:(61*2)+1]
      print(f"dir_first = {dir_first} and dir_next = {dir_next} and {dir_first==dir_next}")
      y = input("enter a key: ")
    
  path.append(next_path)
  #print(path)
  #y = input("enter a key: ")
  step+=1
  if step==length-1:
    instructions*=2
    length=len(instructions)
  elif node[2]=="Z":
    break

print(path, len(path))


  
"""
#this should go inside the while loop
  node_starts = np.array([move(node, next) for node in node_starts])
  step += 1
  ends = np.array[node[2]=="Z" for node in node_starts]
  if step == length-2:
    instructions = instructions * 2
    length = len(instructions)
  if all(ends):
    break"""


  


  
  
