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
  findType=[]
  findType = {i:sum([i==x for x in hand]) for i in hand if i not in findType}
  #print(f"{findType}")
  values = list(findType.values())
  #print(f"values {values} ")
  if 5 in values:
    type = "fiveKind"
    #print(f"{type}")
  elif 4 in values:
    type = "fourKind"
    #print(f"{type}")
  elif 3 in values and 2 not in values:
    type = "threeKind"
    #print(f"{type}")
  elif 3 in values and 2 in values:
    type = "fullHouse"
    #print(f"{type}")
  elif values.count(2)==2:
    type = "twoPair"
    #print(f"{type}")
  elif values.count(2)==1:
    type = "onePair"
    #print(f"{type}")
  else:
    type = "highCard"
  return type
  

def asRank4two(hand1, hand2):
  rank1, rank2 = 0, 0
  #print(f"hand1 = {hand1} and hand2 = {hand2} ")
  for card1, card2 in zip(hand1, hand2):
    #print(f"card1 = {card1} and card2 = {card2} ")
    value1, value2 = card2value[card1], card2value[card2]
    if value1 > value2 : rank1+=1
    elif value1 < value2 : rank2+=1
    #print(f"rank1 = {rank1} and rank2 = {rank2} ")
    if rank1> rank2 or rank2 > rank1: return rank1, rank2
  return rank1, rank2

hands_dict = readFile2Data()

#hands_dict={"32T3K": [765], "T55J5": [684], "KK677": [28], "KTJJT": [220], "QQQJA": [483]}
hands = list(hands_dict.keys())
#print(f"hands {hands} ")
bids = list(hands_dict.values())

card2value = {card:value for card, value in zip("23456789TJQKA", range(1,14))}
#print(card2value["A"])

typeforHands_lst = list(map(findTypeHand, hands))
typesHands = [(hand, findTypeHand(hand)) for hand in hands]
#print(f"typesHands {typesHands} ")
#typesforHands_indices = list(enumerate(typeforHands_lst))
#print(f"typeforHands_lst {typeforHands_lst}")

types = ("highCard", "onePair", "twoPair", "threeKind", "fullHouse", "fourKind", "fiveKind")


# Combine hands and typeforHands_lst into a single iterable for reuse
#hads_types_tuples = list(zip(hands, typeforHands_lst))
#print(f"combined_data = {hads_types_tuples} ")
# Store the counts of each type for reuse
type_counts = {t: typeforHands_lst.count(t) for t in types}
#print(f"type_counts {type_counts}")

secOrder = {
    t: [h for h, type_ in typesHands if type_ == t] 
    for t in types if any(type_ == t for _, type_ in typesHands)
}
#print(f"secOrder {secOrder}")

rank=0

for type in secOrder:
  if len(secOrder[type]) == 1:
    rank+=1
    #print(secOrder[type][0])
    #print(hands_dict[secOrder[type][0]])
    hands_dict[secOrder[type][0]].append(rank)
    #print(hands_dict[secOrder[type][0]])
  else:
    #print(type, secOrder[type])
    for i in range(1, len(secOrder[type])):
      #print(f"calling {secOrder[type][i-1]} and {secOrder[type][i]} ")
      rank1, rank2 = asRank4two(secOrder[type][i-1], secOrder[type][i])
      hands_dict[secOrder[type][i-1]].append(rank+rank1+1)
      hands_dict[secOrder[type][i]].append(rank+rank2+1)
      rank+=2
      #print(hands_dict[secOrder[type][i-1]], hands_dict[secOrder[type][i]])

bids_rank = list(hands_dict.values())
print(bids_rank)

result = sum([bid*rank for (bid, rank) in bids_rank])
print(result)
