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
