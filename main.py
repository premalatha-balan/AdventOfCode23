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

def getRank4Pairs(type):
  return



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


typeforHands_lst = list(map(findTypeHand, hands))
typesforHands_indices = list(enumerate(typeforHands_lst))
print(typeforHands_lst)

types = ("highCard", "onePair", "twoPair", "threeKind", "fullHouse", "fourKind", "fiveKind")

#secOrder ={(type:[].append(hands[i]) if type in typeforHands_lst and typeforHands_lst.count(type)>1 for type in types) for i in range(len(hands)) }


#secOrder = {type: [hands[i] for i in range(len(hands)) if type in typeforHands_lst and typeforHands_lst.count(type) > 1] for type in types}
#print(f"secOrder = {secOrder}")
secOrder = {type:[] for type in typeforHands_lst}


secOrder = defaultdict(list)


secOrder = {t: [h for h, type in zip(hands, typeforHands_lst) if type == t] 
            for t in types if typeforHands_lst.count(t) > 1}


"""for t, h in zip(typeforHands_lst, hands):
    if t in types and typeforHands_lst.count(t) > 1:
        secOrder[t].append(h)"""

#secOrder = dict(secOrder)

"""
for type in types:
  if type in typeforHands_lst and typeforHands_lst.count(type)>1:
    for i in range(len(hands)):
      secOrder[type].append(hands[i]) if typeforHands_lst[i]==type else None"""
      
print(secOrder)

#hands_dict = {hands_dict[i]: bids[i] for i in range(len(hands_dict))}}


"""for i in range(len(typeforHands_lst)):
  print(f"{hands[i]} {typeforHands_lst[i]}")
  #hands_dict[hands[i]]+="".join(typeforHands[i])
  hands_dict[hands[i]].append(typeforHands_lst[i]) #enable if needed
  #print(f"{hands_dict[hands[i]]}")"""
  

