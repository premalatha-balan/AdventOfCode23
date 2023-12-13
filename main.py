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

step = 0
path=[]
length = len(instructions)
node=node_starts[0]
matches = {}
while True:
  dir = instructions[step]
  neighbour = data[node]
  #next_path = (neighbour, dir)
  if neighbour  in path:
    print(f"yes, we have a match")
    #matches.append(path.index(neighbour))
    match_posn = path.index(neighbour)
    matches.update({neighbour:(match_posn, step)})
    print(f"matches {matches} ")
    y = input("enter a key: ")
    if length<step+step:
      instructions=instructions*2
      length = len(instructions)
    for i in range(0,step):
      dir = instructions[i]
      if dir == instructions[step+i]:
        print(neighbours_lst[i], neighbours_lst[step+i], i)

        y = input("enter a key: ")
        match_move = i 
      else:
        break

    print(node)
    node = node_lst[match_move]
    print(f"match move {match_move}, node = {node} ")
    y = input("enter a key: ")
    
        
        

  path.append(neighbour)
  #print(f"path {path}")
  next = 0 if dir == "L" else 1
  node = data[node][next]
  step+=1
  if step==length-2:
    instructions=instructions*2
    length=len(instructions)
  elif node[2]=="Z":
    print(f"reached the end {node} at {step} ")
    y = input("enter a key: ")
    break