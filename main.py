

def readFile2Data():
  f=open("day8_input.txt", "r")
  
  data = [line.strip() for line in f]
  instructions = data[0]
  #print(instructions)
  #y = input("enter a key: ")
  data.pop(0)
  data.pop(0)
  #data.pop(1)
  #data.pop(2)
  #data.pop(3)
  data = [line.split(" ") for line in data]
  data = {line[0] : (line[2].strip("(,"), line[3].strip(")")) for line in data}
  #data = { line[0]:line[2].strip(",").split(", ") for line in data}
  #new={}
  #for line in data:
    #print(line, len(line), data.index(line))
    #y = input("enter a key: ")
    #for i in range(len(line)):
      #print(line[i])
      #y = input("enter a key: ")
    #new.update({line[0]:(line[2][0].strip(","), line[2][-1])})
  #print(data)
  #y = input("enter a key: ")
  f.close
  return(instructions, data)

instructions, data = readFile2Data()

#"L","R"=0,1
#print(instructions)
#print(len(instructions))
node = "AAA"
step=0
"""for i in instructions:
  print(f"entering in node = {node} direction now = {i}, len {len(instructions)} ")
  next = 0 if i=="L" else 1
  node = data[node][next]
  step+=1
  if node=="ZZZ": break
  else:
    if step==len(instructions)-2: 
      print(f"I am here at {step}, dir ={i} and node = {node} ")
      y = input("enter a key: ")
      instructions=instructions + instructions
      print(f"len = {len(instructions)} ")
  if step>=266:
    print(f"next node = {node} in steps {step} ")
    y = input("enter a key: ")"""

while node!="ZZZ":
  i=instructions[step]
  #print(f"entering in node = {node} direction now = {i}, len {len(instructions)} ")
  next = 0 if i=="L" else 1
  node = data[node][next]
  step+=1
  if node=="ZZZ": break
  else:
    if step==len(instructions)-2: 
      #print(f"I am here at {step}, dir ={i} and node = {node} ")
      #y = input("enter a key: ")
      instructions=instructions + instructions
      #print(f"len = {len(instructions)} ")
  #if step>=266:
  #print(f"next node = {node} in steps {step} ")
  #y = input("enter a key: ")
    
print(step)