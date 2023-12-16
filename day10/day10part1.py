import numpy as np
import copy
import math

def readFile2Data():
  f=open("day10_input.txt", "r")
  tile_row = []
  tiles=np.array([])
  #tiles = np.array(tile2Dlst)
  count = 0
  tile_row = ["." for i in range(142)]
  tiles = np.r_[tiles, tile_row]
  for line in f:
    line=line.strip().split()
    for i in line:
      tile_row = [c for c in i]
      tile_row.insert(0, ".")
      tile_row.append(".")
      tiles = np.r_[tiles, tile_row]
      #tiles = np.append(tiles,tile_row) #does the same too
      count+=1
  length = len(tile_row)
  tile_row = ["." for i in range(length)]
  tiles = np.r_[tiles,tile_row]
  tiles = tiles.reshape(count+2, length)
  print(tiles.shape)
  #print(tile2Dlst.shape)
  #tile2Dlst = np.array(tile2Dlst)
  f.close
  return tiles


def check_bounds(yin,xin, r, c):
  if yin+1>=r  or yin-1<0 or xin+1>=c or xin-1<0 : return False
  else: return True


def get_neigh(el,y,x):
  neigh=np.array([[tiles[y-1][x-1],tiles[y-1][x],tiles[y-1][x+1]], [tiles[y][x-1],tiles[y][x],tiles[y][x+1]], [tiles[y+1][x-1],tiles[y+1][x],tiles[y+1][x+1]]])
  return neigh

"""def get_neigh(el,y,x):
  neigh=np.array([[tiles[y-1][x-1],tiles[y-1][x],tiles[y-1][x+1]], [tiles[y][x-1],tiles[y][x],tiles[y][x+1]], [tiles[y+1][x-1],tiles[y+1][x],tiles[y+1][x]]])
  return neigh"""

#starting
def get_move_start(neigh):
  connected = connect(neigh)
  y1,x1 = 0,0
  y2,x2 = 0,0
  

  if connected[0][1]: #up
    pipe = neigh[0][1]
    yl,xl=0,0
    if pipe=="|" or pipe =="F" or pipe=="7": yl-=1 #down move to [0][1]
    #code below moved two steps at once at corners. 
    #if pipe == "|": yl-=1 #down move to [0][1]
    #elif pipe == "F": yl,xl = yl-1, xl+1 #rightUp move to [0][2]
    #elif pipe == "7":  yl,xl = yl-1, xl-1  #leftUp move to [0][0]
    y1,x1 = yl, xl #if condtion checking is not necessary as y1==0 and x1==0 
  if connected[1][0]: #left
    pipe = neigh[1][0]
    yl,xl=0,0
    if pipe=="-" or pipe =="F" or pipe=="L": xl-=1 #left move to [1][0]
    #code below moved two steps at once at corners.
    #if pipe == "-": xl-=1 #left move to [1][0]
    #elif pipe == "F": yl,xl = yl+1, xl-1  #leftDown move to [2][0]
    #elif pipe == "L": yl,xl = yl-1, xl-1  #leftUp move to [0][0]
    if y1==0 and x1==0: y1,x1 = yl, xl
    else: y2,x2 = yl, xl
  
  if connected[1][2]: #right
    pipe = neigh[1][2]
    yl,xl=0,0
    if pipe=="-" or pipe=="7" or pipe=="J": xl+=1 #right move to [1][2]
    #code below moved two steps at once at corners.
    #if pipe == "-": xl+=1 #right move to [1][2]
    #elif pipe == "7": yl,xl = yl+1, xl+1 #rightDown move to [2][2]
    #elif pipe == "J":  yl,xl = yl-1, xl+1 #rightUp move to [0][2]
    if y1==0 and x1==0: y1,x1 = yl, xl
    else: y2,x2 = yl, xl
  if connected[2][1]: #down
    pipe = neigh[2][1]
    yl,xl=0,0
    if pipe=="|" or pipe=="J" or pipe=="L": yl+=1 #down move to [2][1]
    #code below moved two steps at once at corners.
    #if pipe == "|": yl+=1#down move to [2][1]
    #elif pipe == "J": yl,xl = yl+1, xl-1 #leftDown move to [2][0]
    #elif pipe == "L": yl,xl = yl+1, xl+1 #leftUp move to [2][2]
    if y1==0 and x1==0: y1,x1 = yl, xl
    else: y2,x2 = yl, xl
  
  return (y1,x1,y2,x2)

  #generic one #assuming there is only one path
def get_move(neigh):
  connected = connect(neigh)
  y1,x1=0,0
  yl,xl=0,0
  #cy1,cx1 = 0,0 #do not need to return this, as we were moving twice and markign them without counting.

  if connected[0][1]: #up
    pipe = neigh[0][1]
    if pipe=="|" or pipe =="F" or pipe=="7": yl-=1 #down move to [0][1]
    #code below moved two steps at once at corners. 
    #if pipe == "|": yl-=1 #up move to [0][1]
    #elif pipe == "F": yl,xl = yl-1, xl+1 #rightUp move to [0][2]
    #elif pipe == "7":  yl,xl = yl-1, xl-1  #leftUp move to [0][0]
    y1,x1 = yl, xl #if condtion checking is not necessary as y1==0 and x1==0 
    #cy1,cx1=-1,0 #needed to change to the additive values to get to that position rather than the position itself
  elif connected[1][0]: #left
    #tiles[y+1][x] = "S"
    pipe = neigh[1][0]
    if pipe=="-" or pipe=="F" or pipe=="L": xl-=1 #left move to [1][0]
    #code below moved two steps at once at corners.
    #if pipe == "-": xl-=1 #left
    #elif pipe == "F": yl,xl = yl+1, xl-1  #leftDown move to [2][0]
    #elif pipe == "L": yl,xl = yl-1, xl-1  #leftUp move to [0][0]
    y1,x1 = yl, xl
    #cy1,cx1=0,-1 #needed to change to the additive values to get to that position rather than the position itself
  elif connected[1][2]: #right
    pipe = neigh[1][2]
    if pipe=="-" or pipe=="7" or pipe=="J": xl+=1 #right move to [1][2]
    #code below moved two steps at once at corners.
    #if pipe == "-": xl+=1 #right move to [1][2]
    #elif pipe == "7": yl,xl = yl+1, xl+1 #rightDown move to [2][2]
    #elif pipe == "J":  yl,xl = yl-1, xl+1 #rightUp move to [0][2]
    y1,x1 = yl, xl
    #cy1,cx1=0,1 #needed to change to the additive values to get to that position rather than the position itself
  elif connected[2][1]: #down
    pipe = neigh[2][1]
    if pipe=="|" or pipe=="J" or pipe=="L": yl+=1 #down move to [2][1]
    #code below moved two steps at once at corners.
    #if pipe == "|": yl+=1#down move to [2][1]
    #elif pipe == "J": yl,xl = yl+1, xl-1 #leftDown move to [2][0]
    #elif pipe == "L": yl,xl = yl+1, xl+1 #leftUp move to [2][2]
    y1,x1 = yl, xl
    #cy1,cx1=1,0 #needed to change to the additive values to get to that position rather than the position itself

  return (y1,x1)
  
  """
  left = moves[y][x-1]
  right = moves[y][x+1]
  up = moves[y-1][x]
  down = moves[y+1][x]
  leftUp = moves[y-1][x-1]
  leftDown = moves[y+1][x-1]
  rightUp = moves[y-1][x+1]
  rightDown = moves[y+1][x+1]
  noMove = moves[y][x]
  
  if pipe == "-": left or right
  if pipe == "|": up or down
  if pipe == "L": leftUp or rightDown
  if pipe == "F" : rightUp or leftDown
  if pipe == "J": leftDown or rightUp
  if pipe == "7": rightDown or leftUp
  if pipe == ".": noMove"""



"""def connect (neigh):
  centre = neigh[1][1] if neigh[1][1]!="S" else "7"
  #connected= np.array([[None,None, None], [None,centre, None], [None,None, None]])
  #check these connections first draw all these and check
  left = neigh[1][0] if centre == "-" or centre == "J" or centre == "7" else None
  right = neigh[1][2]  if centre == "-" or centre == "L" or centre == "F" else None
  up = neigh[0][1] if centre == "|" or centre == "J" or centre == "L" else None
  down = neigh[2][1] if centre = "|" or centre == "F" or centre == "7" else None"
  #connected = np.array([[None,None,None], [None,None,None], [None,None,None]])
  left = True if left=="-" or left=="F" or left=="L" else False
  right = True if right=="-" or right=="7" or right=="J" else False
  up = True if up=="|" or up=="F" or up=="7" else False
  down = True if down=="|" or down=="L" or down=="J" else False
  connected = np.array([[None, up, None], [left, None, right,], [None, down, None]])
  return (connected)"""

def connect(neigh):
  centre = neigh[1][1] if neigh[1][1]!="S" else "7"
  connected= np.array([[None,None, None], [None,centre, None], [None,None, None]])
  if centre == "-":
    left = neigh[1][0] 
    right = neigh[1][2]
    connected[1][0] = True if left=="-" or left=="F" or left=="L" else False #left
    connected[1][2] = True if right=="-" or right=="7" or right=="J" else False #right
  elif centre == "|":
    up = neigh[0][1]
    down = neigh[2][1]
    connected[0][1] = True if up=="|" or up=="F" or up=="7" else False #up
    connected[2][1] = True if down=="|" or down=="L" or down=="J" else False #down
  elif centre == "L":
    up = neigh[0][1]
    right = neigh[1][2]
    connected[0][1] = True if up=="|" or up=="F" or up=="7" else False #up
    connected[1][2] = True if right=="-" or right=="7" or right=="J" else False #right
  elif centre == "F":
    right = neigh[1][2]
    down = neigh[2][1]
    connected[1][2] = True if right=="-" or right=="7" or right=="J" else False #right
    connected[2][1] = True if down=="|" or down=="L" or down=="J" else False #down
  elif centre == "J":
    up = neigh[0][1]
    left = neigh[1][0]
    connected[0][1] = True if up=="|" or up=="F" or up=="7" else False #up
    connected[1][0] = True if left=="-" or left=="F" or left=="L" else False #left
  elif centre == "7":
    left = neigh[1][0]
    down = neigh[2][1]
    connected[1][0] = True if left=="-" or left=="F" or left=="L" else False #left
    connected[2][1] = True if down=="|" or down=="L" or down=="J" else False #down
  #print(f"connected = {connected}")
  #z = input("enter a key: ")
  return connected
    
  

#initialising
tiles = readFile2Data()
r, c = tiles.shape
#print(r, c)

y, x = np.where(tiles == "S")
y,x=y[0],x[0]
print(f"start at y,x = {y},{x}")
step=0


#getting data through functions for the starting poistion
neigh = get_neigh(tiles[y,x],y,x) if check_bounds(y,x,r,c) else None
#print(neigh)
y1,x1,y2,x2 = get_move_start(neigh)
#print(f"y1,x1,y2,x2 =  {y1},{x1},{y2},{x2}")
y1,x1,y2,x2 = y+y1, x+x1, y+y2, x+x2
path1, path2= np.array([y1,x1]), np.array([y2,x2])
step+=1 #moved one step
#print(f"step = {step}")
#print(y1,x1,y2,x2)
#print(f"path1 = {path1}, path2 = {path2}")
#z = input("enter a key: ")

#print(check_bounds(y1,x1,r,c))

#start while true loop here
while True:
  #print("\n\nDoing path1")
  neigh = get_neigh(tiles[y1,x1],y1,x1) if check_bounds(y1,x1,r,c) else np.array([[None,None, None], [None,None, None], [None,None, None]])
  #print(neigh)
  y,x=y1,x1
  #print(f"at y,x = {y},{x}")
  y1,x1 = get_move(neigh)
  
  """if (y1!=0 and x1!=0):
    #print(f"change at cy,cx = {cy1},{cx1}")
    cy1,cx1 = y+cy1, x+cx1
    tiles[cy1,cx1] = "S"
    #print(f"changed at y,x = {cy1},{cx1} to {tiles[cy1,cx1]} ")"""
  if y1==0 and x1==0: 
    print("Doing path1 breaking point")
    print(f"neigh = {neigh}")
    print(f"at y,x = {y}, {x}")
    #print(f"y1,x1 =  {y1},{x1}")
    #z = input("enter a key: ")
    break #if no more moves
  #print(f"y1,x1 =  {y1},{x1}")
  y1,x1 = y+y1, x+x1
  path1= np.array([y1,x1])
  tiles[y,x]= "S"
  #print(y1,x1)
  #print(f"path1 = {path1}")
  #z = input("enter a key: ")
  
  #print("\n\nNow doing path2")
  neigh = get_neigh(tiles[y2,x2],y2,x2) if check_bounds(y2,x2,r,c) else np.array([[None,None, None], [None,None, None], [None,None, None]]) 
  #need to do cases for the boundary conditions - padded up instead
  #print(neigh)
  y,x=y2,x2
  #print(f"at y,x = {y},{x}")
  y2,x2 = get_move(neigh)
  """if (y2!=0 and x2!=0):
    #print(f"change at cy,cx = {cy2},{cx2}")
    cy2,cx2 = y+cy2,x+cx2
    tiles[cy2,cx2] = "S"
    #print(f"changed at y,x = {cy2},{cx2} to {tiles[cy2,cx2]}")"""
  if y2==0 and x2==0:
    print("Doing path2 breaking point")
    print(f"neigh = {neigh}")
    print(f"at y,x = {y},{x}")
    #print(f"y2,x2 =  {y2},{x2}")
    #z = input("enter a key: ")
    break #if no more moves
  #print(f"y2,x2 =  {y2},{x2}")
  y2,x2 = y+y2, x+x2
  path2= np.array([y2,x2])
  tiles[y,x]= "S"
  #print(y2,x2)
  #print(f"path2 = {path2}")
  #z = input("enter a key: ")
  
  #counting steps & setting up before next move
  #tiles[cy1,cx1] = "S"
  #print(f"changed at y,x = {cy1},{cx1} to {tiles[cy1,cx1]} ")
  #tiles[cy2,cx2] = "S"
  #print(f"changed at y,x = {cy2},{cx2} to {tiles[cy2,cx2]}")
  step+=1 #moved one step
  #print(f"step = {step}")
  #z = input("continuing the while loop. enter a key: ")
  
  #checking if the paths are the same
  #if no more moves, then we should have reached the converging point of path1 and path2

print(f"step = {step}")

#change the hardcoded value for S in connect and the length of each line in readfile2data