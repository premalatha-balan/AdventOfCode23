
f=open("day2_input.txt", "r")

bag = [("red", 12),  ("blue",14), ("green", 13)]
l = 1
Games ={}
SumPowers=0
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
  #print(f"Games[{game}] {Games[game]}" )

  reds,blues,greens = 0,0,0
  for i in range(1,len(Games[game])):
    if "red" in Games[game][i]: reds = max(reds,Games[game][i][1])
    if "blue" in Games[game][i]: blues = max(blues,Games[game][i][1])
    if "green" in Games[game][i]: greens = max(greens,Games[game][i][1])
  #print(f"{game}: reds {reds} blues {blues} greens {greens}")
  #y = input("enter a key: ")

  gamePower = reds*blues*greens
  SumPowers+=gamePower
  
  l+=1 #end of for loop
  
print(SumPowers)  

f.close

