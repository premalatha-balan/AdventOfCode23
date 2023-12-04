
f=open("day2_input.txt", "r")

bag = [("red", 12),  ("blue",14), ("green", 13)]
l = 1
Games ={}
Sum=0
for line in f:
  line=line.strip()
  start = line.find(":")
  game = line[:start].strip("")
  Games[game]=[l]
  reveals = line[start+1:].split("; ")
  for reveal in reveals:
    reveal_lst = reveal.strip(" ").split(",")
    for ball in reveal_lst:
      ball=ball.strip()
      num, color = ball.split(" ")
      number = int(num)
      Games[game].append((color, number))

  for game in Games:
    reds,blues,greens = 0,0,0
    for i in range(1,len(Games[game])):
      if "red" in Games[game][i]: reds = max(reds,Games[game][i][1])
      if "blue" in Games[game][i]: blues = max(blues,Games[game][i][1])
      if "green" in Games[game][i]: greens = max(greens,Games[game][i][1])

  gameId = Games[game][0]
  if reds<= bag[0][1] and blues <= bag[1][1] and greens <= bag[2][1]:
    Sum+=gameId

  l+=1 #end of for loop

print(Sum)  

f.close

