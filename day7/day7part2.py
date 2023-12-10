def readFile2Data():
  f=open("day7_input.txt", "r")
  hands_dict={}
  hands_dict = {(line.strip().split())[0]: [int((line.strip().split())[1])] for line in f}
  f.close
  return(hands_dict)

  
def findTypeHand(hand):
  findType=[]
  findType = {i:sum([i==x for x in hand]) for i in hand if i not in findType}
  values = list(findType.values())
  if 5 in values:
    type = "fiveKind"
  elif 4 in values:
    type = "fiveKind" if "J" in hand else "fourKind"
  elif 3 in values and 2 not in values:
    if "J" in hand:
      if hand.count("J") == 1 or hand.count("J") == 3: type = "fourKind"
      if hand.count("J") == 2: type = "fiveKind"
      
    else: 
      type = "threeKind"
  elif 3 in values and 2 in values:
    type = "fiveKind" if "J" in hand else "fullHouse"
  elif values.count(2)==2:
    type = "twoPair"
    if "J" in hand:
      if hand.count("J") == 1: type = "fullHouse"
      if hand.count("J") == 2: type = "fourKind"
  elif values.count(2)==1:
    type = "threeKind" if "J" in hand and (hand.count("J") == 1 or hand.count("J") == 2) else "onePair"
  else:
    type = "onePair" if "J" in hand else "highCard"
  return type
  

def compare(hand1, hand2):
  rank1, rank2 = 0, 0
  for card1, card2 in zip(hand1, hand2):
    value1, value2 = card2value[card1], card2value[card2]
    if value1 < value2 : return True
    elif value1 > value2 : return False 


def qSort(inList):
  if len(inList) <= 1:
    return inList
  else:
    pivot = inList[0]
    left = [x for x in inList[1:] if compare(x, pivot)]
    right = [x for x in inList[1:] if not compare(x, pivot)]
    return qSort(left) + [pivot] + qSort(right)


hands_dict = readFile2Data()

#hands_dict={"32T3K": [765], "T55J5": [684], "KK677": [28], "KTJJT": [220], "QQQJA": [483]}
hands = list(hands_dict.keys())
bids = list(hands_dict.values())

card2value = {card:value for card, value in zip("J23456789TQKA", range(1,14))}

typeforHands_lst = list(map(findTypeHand, hands))
#print(f"tpyeforHands_lst {typeforHands_lst}")
typesHands = [(hand, findTypeHand(hand)) for hand in hands]


types = ("highCard", "onePair", "twoPair", "threeKind", "fullHouse", "fourKind", "fiveKind")

# Combine hands and typeforHands_lst into a single iterable for reuse
#typesHands = [(hand, findTypeHand(hand)) for hand in hands]
#print(f"typesHands = {typesHands} ")
# Store the counts of each type for reuse
type_counts = {t: typeforHands_lst.count(t) for t in types}
#print(f"type_counts {type_counts}")

secOrder = {
  t: [h for h, type_ in typesHands if type_ == t] 
  for t in types if any(type_ == t for _, type_ in typesHands)
}

rank=0


secOrder = {t: qSort(secOrder[t]) for t in secOrder}


rank = 1
for card_type in secOrder:
    for index, card in enumerate(secOrder[card_type]):
        hands_dict[card].append(rank + index)
    rank += len(secOrder[card_type])

    

bids_rank = list(hands_dict.values())
#print(bids_rank)

result = sum([bid*rank for (bid, rank) in bids_rank])
print(result)
