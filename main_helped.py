from collections import defaultdict

def findTypeHand(hand):
  findType=[]
  findType = {i: sum([i == x for x in hand]) for i in hand if i not in findType}
  values = list(findType.values())
  if 5 in values:
      return "fiveKind"
  elif 4 in values:
      return "fourKind"
  elif 3 in values and 2 not in values:
      return "threeKind"
  elif 3 in values and 2 in values:
      return "fullHouse"
  elif values.count(2) == 2:
      return "twoPair"
  elif values.count(2) == 1:
      return "onePair"
  else:
      return "highCard"

def asRank4two(hand1, hand2, rank):
  for card1, card2 in zip(hand1, hand2):
    value1, value2 = card2value[card1], card2value[card2]
    if value1 > value2:
        rank += 1
    elif value1 < value2:
        rank += 2
    # Increment rank by 1 regardless of values
    rank += 1
  return rank




hands_dict = {"32T3K": [765], "T55J5": [684], "KK677": [28], "KTJJT": [220], "QQQJA": [483]}
hands = list(hands_dict.keys())
types = ("highCard", "onePair", "twoPair", "threeKind", "fullHouse", "fourKind", "fiveKind")
card2value = {card: value for card, value in zip("23456789TJQKA", range(1, 14))}

typesHands = [(hand, findTypeHand(hand)) for hand in hands]

secOrder = {t: [h for h, type_ in typesHands if type_ == t] for t in types if any(type_ == t for _, type_ in typesHands)}

rank = 0

for hand_type in secOrder.keys():
    if len(secOrder[hand_type]) == 1:
        rank += 1
        hands_dict[secOrder[hand_type][0]].append(rank)
    else:
        for i in range(1, len(secOrder[hand_type])):
            rank = asRank4two(secOrder[hand_type][i-1], secOrder[hand_type][i], rank)
            hands_dict[secOrder[hand_type][i-1]].append(rank)
            hands_dict[secOrder[hand_type][i]].append(rank)

bids_rank = list(hands_dict.values())
result = sum(bid * rank for bid, rank in bids_rank)
print(result)
