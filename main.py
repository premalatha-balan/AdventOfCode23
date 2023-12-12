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
matches = []
while True:
  dir = instructions[step]
  neighbour = data[node]
  #next_path = (neighbour, dir)
  if neighbour  in path:
    print(f"yes, we have a match")
    matches.append(path.index(neighbour))
    print(f"matches {matches} ")
    y = input("enter a key: ")
    if len(matches)>1:
      match_length = matches[1]-matches[0]
      dir_first = instructions[matches[0]:matches[1]]
      dir_next = instructions[matches[1]:matches[1]+matches[1]]
      print(f"dir_first = {dir_first} and dir_next = {dir_next}")
      print(f"{dir_first==dir_next}")
      y = input("enter a key: ")

  path.append(neighbour)
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