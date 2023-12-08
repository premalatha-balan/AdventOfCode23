"""
def readFile2Data():
 
  f.close"""

#ile2DreadFata()


types = {5: "fiveKind",
       4:"fourKind",
       3:"threeKind",
      32:"fullHouse",
       2:"twoPair",
       1:"onePair",
       0:"highCard"}

def chkType (hand):
  type = "fiveKind" if all(hand.count(i) == 5 for i in hand) else "fourKind"
  type = "fourKind" if all(hand.count(i) == 4 for i in hand) else "threeKind"
  type = "FullHouse" if all(hand.count(i) == 3 for i in hand) and if all(hand.count(i) == 2 for i in hand) else "threeKind"
  type = "twoPair" if all(hand.count(i) == 2 for i in hand) and if all(hand.count(i) == 2 for i in hand) else "threeKind"
  type = "onePair" if all(hand.count(i) == 2 for i in hand) and if all(hand.count(i) == 2 for i in hand) else "threeKind"

  return type


def winner(hand1, hand2):
  if hand1>hand2:
    return 1
  elif hand1<hand2:
    return 2
  else:
    return 0

hands=[("32T3K", 765), ("T55J5", 684), ("KK677", 28), ("KTJJT", 220), ("QQQJA", 483)]
for hand in hands:
  #print(f"{hand[0]} {hand[1]} {chkType(hand[0])} {chkType(hand[1])} {winner(hand[1],hand[0])}")  
  print(hand, chkType(hand[0]))

"""for i in hand:
  if hand.count(i) == 3:
    newstr = "".join([j for j in hand if j != i])
    type = "fullHouse" if newstr.count(i) == 2 else "threeKind"
  elif hand.count(i) == 2:
    newstr = "".join([j for j in hand if j != i])
    #type = "twoPair" if newstr.count(i) == 2 else "onePair"
    print(newstr, i)
  else:
    type = "highCard""""