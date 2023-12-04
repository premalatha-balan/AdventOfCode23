
def match (winCard, playCard):
  matches = 0
  for i in range(len(playCard)):
    if playCard[i] in winCard:  
      matches+=1  
  return matches

def instanceMaking(match_lst):
  for k in range(len(match_lst)):
    m = match_lst[k]
    inst = instances[k]
    for i in range(k+1,m+k+1):
      instances[i]+=inst #add the instances by inst times for next m cs
  return instances


f=open("day4_input.txt", "r")

match_lst=[]
instances=[]

l = 0
for line in f:
  line = line.strip()
  winCard = []
  playCard = []
  winC_start = line.find(":")
  playC_start = line.find("|")
  winCard = line[winC_start+1:playC_start].split()
  playCard = line[playC_start+1:].split()

  matches = match(winCard, playCard)
  match_lst.append(matches)
  instances.append(1)

instances = instanceMaking(match_lst)
print(sum(instances))


f.close

