from collections import defaultdict

"""
def readFile2Data():
 
  f.close"""

#ile2DreadFata()

def findTypeHand(hand):
  print(hand)
  findType=[]
  findType = {i:sum([i==x for x in hand]) for i in hand if i not in findType}
  print(f"{findType}")
  values = list(findType.values())
  print(f"values {values} ")
  if 5 in values:
    type = "fiveKind"
    print(f"{type}")
  elif 4 in values:
    type = "fourKind"
    print(f"{type}")
  elif 3 in values and 2 not in values:
    type = "threeKind"
    print(f"{type}")
  elif 3 in values and 2 in values:
    type = "fullHouse"
    print(f"{type}")
  elif values.count(2)==2:
    type = "twoPair"
    print(f"{type}")
  elif values.count(2)==1:
    type = "onePair"
    print(f"{type}")
  else:
    type = "highCard"
  return type
  

def asRank4two(hand1, hand2):
  rank1, rank2 = 0, 0
  print(f"hand1 = {hand1} and hand2 = {hand2} ")
  for card1, card2 in zip(hand1, hand2):
    print(f"card1 = {card1} and card2 = {card2} ")
    value1, value2 = card2value[card1], card2value[card2]
    if value1 > value2 : rank1+=1
    elif value1 < value2 : rank2+=1
    print(f"rank1 = {rank1} and rank2 = {rank2} ")
    if rank1> rank2 or rank2 > rank1: return rank1, rank2
  return rank1, rank2



def winner(hand1, hand2):
  if hand1>hand2:
    return 1
  elif hand1<hand2:
    return 2
  else:
    return 0

#hands=[("32T3K", 765), ("T55J5", 684), ("KK677", 28), ("KTJJT", 220), ("QQQJA", 483)]
hands_dict={"32T3K": [765], "T55J5": [684], "KK677": [28], "KTJJT": [220], "QQQJA": [483]}
hands = list(hands_dict.keys())
bids = list(hands_dict.values())

card2value = {card:value for card, value in zip("23456789TJQKA", range(1,14))}
print(card2value["A"])

typeforHands_lst = list(map(findTypeHand, hands))
typesforHands_indices = list(enumerate(typeforHands_lst))
print(typeforHands_lst)

types = ("highCard", "onePair", "twoPair", "threeKind", "fullHouse", "fourKind", "fiveKind")

#secOrder ={(type:[].append(hands[i]) if type in typeforHands_lst and typeforHands_lst.count(type)>1 for type in types) for i in range(len(hands)) }


#secOrder = {type: [hands[i] for i in range(len(hands)) if type in typeforHands_lst and typeforHands_lst.count(type) > 1] for type in types}
#print(f"secOrder = {secOrder}")  



"""secOrder = defaultdict(list)


secOrder = {t: [h for h, type in zip(hands, typeforHands_lst) if type == t] 
            for t in types if typeforHands_lst.count(t) > 1 }"""


secOrder = defaultdict(list)

secOrder = {t: [h for h, type in zip(hands, typeforHands_lst) if type == t] 
            for t in types if any(type == t for type in typeforHands_lst)}

print(secOrder)

rank=0

for type in secOrder:
  if len(secOrder[type]) == 1:
    rank+=1
    print(secOrder[type][0])
    print(hands_dict[secOrder[type][0]])
    hands_dict[secOrder[type][0]].append(rank)
    print(hands_dict[secOrder[type][0]])
  else:
    print(type, secOrder[type])
    for i in range(1, len(secOrder[type])):
      print(f"calling {secOrder[type][i-1]} and {secOrder[type][i]} ")
      rank1, rank2 = asRank4two(secOrder[type][i-1], secOrder[type][i])
      hands_dict[secOrder[type][i-1]].append(rank+rank1+1)
      hands_dict[secOrder[type][i]].append(rank+rank2+1)
      rank+=2
      
      
      #rank1, rank2 = asRank4two(hands_dict[secOrder[type][i-1]], hands_dict[secOrder[type][i]])
      print(hands_dict[secOrder[type][i-1]], hands_dict[secOrder[type][i]])
      #y = input("enter a key: ")

bids_rank = list(hands_dict.values())


result = sum([bid*rank for (bid, rank) in bids_rank])
print(result)

    





#for type in secOrder:
#  asRank4two(secOrder[type][0], secOrder[type][1], rank+1, rank+1)

"""for t, h in zip(typeforHands_lst, hands):
    if t in types and typeforHands_lst.count(t) > 1:
        secOrder[t].append(h)"""

#secOrder = dict(secOrder)

"""
for type in types:
  if type in typeforHands_lst and typeforHands_lst.count(type)>1:
    for i in range(len(hands)):
      secOrder[type].append(hands[i]) if typeforHands_lst[i]==type else None"""
      


#hands_dict = {hands_dict[i]: bids[i] for i in range(len(hands_dict))}}


"""for i in range(len(typeforHands_lst)):
  print(f"{hands[i]} {typeforHands_lst[i]}")
  #hands_dict[hands[i]]+="".join(typeforHands[i])
  hands_dict[hands[i]].append(typeforHands_lst[i]) #enable if needed
  #print(f"{hands_dict[hands[i]]}")"""
  

