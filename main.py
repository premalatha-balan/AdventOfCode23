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
  return [(lst[i]-lst[i-1]) for i in range(1, len(lst))]

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

sumTot = 0
seqBigLst = readFile2Data()
for line in seqBigLst:
  diffLst = get_diffLst(line)
  #print(diffLst)
  #y = input("enter a key: ")
  #diffLst = [l+[0] if (len(l)>1 and all(l)) else l+l for l in diffLst]
  diffLst[-1].append(diffLst[-1][0]) if all(diffLst[-1]) else diffLst[-1].append(0)
  #diffLst[-1].append(0)
  #print(f"{diffLst} after appending")

  for i in range(len(diffLst)-2,-1,-1):
    #print(diffLst[i])
    diffLst[i].append(diffLst[i][-1]+diffLst[i+1][-1])
    #print(f"{diffLst[i]} after appending the addition")
    #y = input("enter a key: ")

  #diffLst[:-1] = [diffLst[i]+ [diffLst[i][-1]+diffLst[i+1][-1]] for i in range(len(diffLst)-2,-1,-1) ]
  #diffLst.pop(-1)

  
  sumTot+=diffLst[0][-1]


print(sumTot)