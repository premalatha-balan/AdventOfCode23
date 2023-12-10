import copy

def readFile2Data():
  f=open("day9_input.txt", "r")
  #for line in f:
    #line = line.strip().split()
    #print(line)
    #y = input("enter a key: ")
  seqBigLst = [line.strip().split() for line in f]
  seqBigLst = [list(map(int, seq)) for seq in seqBigLst]
  
  f.close
  return(seqBigLst)

def diff(lst):
  return [abs(lst[i]-lst[i-1]) for i in range(1, len(lst))]

def get_diffLst(lst):
  #print(lst)
  diffLst = [[]]
  diffLst[0] = copy.deepcopy(lst)
  #print(diffLst)
  while (any(lst) and len(lst)>1):
    lst = diff(lst)
    #print(lst)
    #y = input("enter a key: ")
    diffLst.append(lst)
    #print(diffLst)
    #y = input("enter a key: ")
  return diffLst

seqBigLst = readFile2Data()
for line in seqBigLst:
  diffLst = get_diffLst(line)
  print(f"{diffLst} outside the function")
  y = input("enter a key: ")
  diffLst = [l+[0] for l in diffLst]
  #diffLst = list(map(_.append(0), diffLst))
  
  print(f"{diffLst} after appending")
  y = input("enter a key: ")
