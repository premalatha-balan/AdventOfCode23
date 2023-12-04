
f=open("day4_input.txt", "r")

score = lambda n: int(2**(n-1))

totalWorth = 0
lcount=1
sCount=0
for line in f:
  line = line.strip()
  winCard = []
  playCard = []
  winC_start = line.find(":")
  playC_start = line.find("|")
  winCard = line[winC_start+1:playC_start].split()
  playCard = line[playC_start+1:].split()
  #print(f"winCard = {winCard} l = {len(winCard)} and playCard = {playCard} l = {len(playCard)} ")
  sCount=0
  #for c in playCard:
  for i in range(len(playCard)):
    c = playCard[i]
    if c in winCard:  
      sCount+=1
      #print(f"{c} in both and so the count = {sCount} ")
  totalWorth+=score(sCount)
  #print(f"totalWorth = {totalWorth} and score = {score(sCount)} for card {lcount} ")
  lcount+=1
  #y = input("enter a key: ")

print(f"totalWorth = {totalWorth} ")
f.close

