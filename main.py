
f=open("day2_input.txt", "r")

#12 red cubes, 13 green cubes, and 14 blue cubes
bag = [("red", 12),  ("blue",14), ("green", 13)]
#print(f"red = {bag[0][1]}")
l = 1
Games ={}
Sum=0
for line in f:
  line=line.strip()
  start = line.find(":")
  game = line[:start].strip("")
  #print(f"game id is {l}")
  Games[game]=[l]
  reveals = line[start+1:].split("; ")
  #print(f"reveals = {reveals} ")
  for reveal in reveals:
    #print(f"reveal = {reveal} ")
    reveal_lst = reveal.strip(" ").split(",")
    #print(f"reveal_lst = {reveal_lst}")
    for ball in reveal_lst:
      ball=ball.strip()
      #print(f"ball = {ball} ")
      num, color = ball.split(" ")
      number = int(num)
      #print(f"num = {num} color = {color} number = {number} ")
      Games[game].append((color, number))
      #print(Games)
      #y = input("enter a key bfr: ")
    #print(f"reveal_lst = {reveal_lst}")
    #print(Games)
    #y = input("enter a key: ")
  l+=1
    
  #print(game, reveals)
  #print(reveal_lst)
  #print(Games)
  #y = input("enter a key 2nd: ")
  #print(f"Games {Games}")
  for game in Games:
    reds,blues,greens = 0,0,0
    #print(f"game = {Games[game]}")
    for i in range(1,len(Games[game])):
      if "red" in Games[game][i]:
        reds = max(reds,Games[game][i][1])
        #print(f"reds = {reds} ")
      if "blue" in Games[game][i]:
        blues = max(blues,Games[game][i][1])
        #print(f"blues = {blues} ")
      if "green" in Games[game][i]:
        greens = max(greens,Games[game][i][1])
        #print(f"greens = {greens} ")
      #y = input("enter a key 5th: ")

  gameId = Games[game][0]
  if reds<= bag[0][1] and blues <= bag[1][1] and greens <= bag[2][1]:
    Sum+=gameId
    #print(f"Sum = {Sum} for gameID = {gameId} ")
    #y = input("enter a key 6th: ")
    #print(f"{game} is the game {gameId} is possible")
    #print(f"reds {reds}, blues {blues} and greens {greens} ")
    #print(f"bag is {bag} ") 
    #y = input("enter a key 4th: ")
    #else:
    #print(f"{game} is the game {gameId} is NOT possible")
    #print(f"Sum = {Sum} for gameID = {gameId} ")
    #print(f"reds {reds}, blues {blues} and greens {greens} ")
    #print(f"bag is {bag} ")
    #y = input("enter a key 4th: ")
  #y = input("enter a key 4th: ")
  #print(f"game {i} = {game}")
  #print(f"game {i} = {game}")
  """for game in Games:
  #print(f"Games[{game}] is {Games[game]}")
  #y = input("enter a key 3rd: ")
  reds,blues,greens = 0,0,0
  for i in range(1,len(Games[game])):
    if "red" in Games[game][i]:
      reds+=Games[game][i][1]
    if "blue" in Games[game][i]:
      blues+=Games[game][i][1]
    if "green" in Games[game][i]:
      greens+=Games[game][i][1]"""
  
print(Sum)  

f.close

