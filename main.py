def readFile2Data():
  f=open("day7_input.txt", "r")
  hands_dict={}
  hands_dict = {(line.strip().split())[0]: [int((line.strip().split())[1])] for line in f}
  #for line in f:
    #line=line.strip().split()
    #print(f"line {line}, {len(line) }")
    #print(line[0], line[1])
    #hands_dict.update( {line[0]: int(line[1])})
    #print(hands_dict)
    #y = input("enter a key: ")
  #print(hands_dict)
  f.close
  return(hands_dict)

  
def findTypeHand(hand):
  #print(hand)
  #hand="JJ28J"
  findType=[]
  findType = {i:sum([i==x for x in hand]) for i in hand if i not in findType}
  #print(f"{findType}")
  #y = input("enter a key: ")
  values = list(findType.values())
  #type="highCard"
  #print(f"values {values} ")
  if 5 in values:
    type = "fiveKind"
    #print(f"{type}")
  elif 4 in values:
    type = "fiveKind" if "J" in hand else "fourKind"
    #print(f"{type}")
  elif 3 in values and 2 not in values:
    #print("I am in here")
    if "J" in hand:
      if hand.count("J") == 1 or hand.count("J") == 3: type = "fourKind"
      if hand.count("J") == 2: type = "fiveKind"
      
    else: 
      type = "threeKind"
    #print(f"{type}")
  elif 3 in values and 2 in values:
    type = "fiveKind" if "J" in hand else "fullHouse"
    #print(f"{type}")
  elif values.count(2)==2:
    type = "twoPair"
    if "J" in hand:
      if hand.count("J") == 1: type = "fullHouse"
      if hand.count("J") == 2: type = "fourKind"
    #print(f"{type}")
  elif values.count(2)==1:
    type = "threeKind" if "J" in hand and (hand.count("J") == 1 or hand.count("J") == 2) else "onePair"
  #print(f"{type}")
  else:
    type = "onePair" if "J" in hand else "highCard"
  #print(f"type {type} ")
  #y = input("enter a key: ")
  #type = "Not in there"
  return type
  

def compare(hand1, hand2):
  #print("I am in asRank4two function")
  #print(f"hand1 {hand1}, hand2 {hand2} ")
  #y=input("enter a key: ")
  rank1, rank2 = 0, 0
  #print(f"hand1 = {hand1} and hand2 = {hand2} ")
  for card1, card2 in zip(hand1, hand2):
    #print(f"card1 = {card1} and card2 = {card2} ")
    value1, value2 = card2value[card1], card2value[card2]
    #value1 = 13 if card1 == "J" else card2value[card]
    if value1 < value2 : return True
    elif value1 > value2 : return False 
    #print(f"rank1 = {rank1} and rank2 = {rank2} ")
  #print(f"rank1 = {rank1} and rank2 = {rank2} ")
  #y=input("enter a key: ")

  

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
#print(f"hands {hands} ")
bids = list(hands_dict.values())
#print(f"bids {bids} ")

card2value = {card:value for card, value in zip("J23456789TQKA", range(1,14))}
#print(f"card2value, {card2value}")

typeforHands_lst = list(map(findTypeHand, hands))
#print(f"tpyeforHands_lst {typeforHands_lst}")
typesHands = [(hand, findTypeHand(hand)) for hand in hands]
#print(f"typesHands {typesHands} ")
#typesforHands_indices = list(enumerate(typeforHands_lst))
#print(f"typeforHands_lst {typeforHands_lst}")

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

"""for type in secOrder:
  print(f"{type}: {secOrder[type]}")
  rank += type_counts[type]
  print(f"rank = {rank}, lenght = {len(secOrder[type])}")
  y = input("enter a key: ")"""
#print(f"Second Order Ranking: {secOrder}" )


rank = 1
for card_type in secOrder:
    for index, card in enumerate(secOrder[card_type]):
        hands_dict[card].append(rank + index)
    rank += len(secOrder[card_type])

    

bids_rank = list(hands_dict.values())
#print(bids_rank)

result = sum([bid*rank for (bid, rank) in bids_rank])
print(result)
