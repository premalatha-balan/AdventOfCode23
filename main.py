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
    for i in range(match_posn,step):
      dirl = instructions[i]
      print(f"dir = {dirl} and instructions[step+i] = {instructions[step+i]} at i = {i} step {step+i} ")
      y = input("enter a key: ")
      if dirl == instructions[step+i]:
        match_move = i+1
        print(f"match_move = {match_move}")
        break
      else:
        break

    print(node)
    print(f"match move {match_move}, node = {node} ")
    print(f"match_posn {match_posn} ")
    y = input("enter a key: ")
    for i in range(match_posn,match_move+1):
      path.append(path[i])
    node_posn = neighbours_lst.index(path[-1])
    node = node_lst[node_posn]
    dir = instructions[step+match_move]
    next = 0 if dir == "L" else 1
    neighbour = neighbours_lst[node_posn]
    step+=(match_move+1)
    print(f"node = {node}, neighbhour = {neighbour} ")
    print(f"path= {path}" )
    y = input("enter a key: ")
    
  else:
    path.append(neighbour)
    step+=1
    next = 0 if dir == "L" else 1
    node = data[node][next]
  
  if step==length-2:
    instructions=instructions*2
    length=len(instructions)
  elif node[2]=="Z":
    print(f"reached the end {node} at {step} ")
    y = input("enter a key: ")
    break