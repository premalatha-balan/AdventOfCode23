import numpy as np
import copy
import math

def readFile2Data():
  f=open("day10_input.txt", "r")
  tile_row = []
  tile2Dlst =[[]]
  tiles=np.array([])
  #tiles = np.array(tile2Dlst)
  count = 0
  for line in f:
    line=line.strip().split()
    for i in line:
      tile_row = [c for c in i]
      tiles = np.r_[tiles,tile_row]
      #tiles = np.append(tiles,tile_row) #does the same too
      count+=1
  length = len(tile_row)
  tiles = tiles.reshape(count, length)
  #print(tiles.shape)
  #print(tile2Dlst.shape)
  #tile2Dlst = np.array(tile2Dlst)
  f.close
  return tiles


def check_bounds(yin,xin, r, c):
  if yin+1>=r  or yin-1<0 or xin+1>=c or xin-1<0 : return False
  else: return True


def get_neigh(el,y,x):
  neigh=np.array([[None,tiles[y-1][x],None], [tiles[y][x-1],tiles[y][x],tiles[y][x+1]], [None,tiles[y+1][x],None]])
  return neigh

"""def get_neigh(el,y,x):
  neigh=np.array([[tiles[y-1][x-1],tiles[y-1][x],tiles[y-1][x+1]], [tiles[y][x-1],tiles[y][x],tiles[y][x+1]], [tiles[y+1][x-1],tiles[y+1][x],tiles[y+1][x]]])
  return neigh"""

def get_move(neigh):
  
  connected = connect(neigh)
  y1,x1 = 0,0
  y2,x2 = 0,0

  if connected[0][1]: #up
    pipe = neigh[0][1]
    yl,xl=0,0
    if pipe == "|": yl-=1 #down move to [0][1]
    elif pipe == "F": yl,xl = yl-1, xl+1 #rightUp move to [0][2]
    elif pipe == "7":  yl,xl = yl-1, xl-1  #leftUp move to [0][0]
  if connected[1][0]: #left
    pipe = neigh[1][0]
    yl,xl=0,0
    if pipe == "-": xl-=1 #left
    elif pipe == "F": yl,xl = yl+1, xl-1  #leftDown move to [2][0]
    elif pipe == "L": yl,xl = yl-1, xl-1  #leftUp move to [0][0]
    if y1==0 and x1==0: y1,x1 = yl, xl
    else: y2,x2 = yl, xl
  if connected[1][2]: #right
    pipe = neigh[1][2]
    yl,xl=0,0
    if pipe == "-": xl+=1 #right move to [1][2]
    elif pipe == "7": yl,xl = yl+1, xl+1 #rightDown move to [2][2]
    elif pipe == "J":  yl,xl = yl-1, xl+1 #rightUp move to [0][2]
    if y1==0 and x1==0: y1,x1 = yl, xl
    else: y2,x2 = yl, xl
  if connected[2][1]: #down
    pipe = neigh[2][1]
    yl,xl=0,0
    if pipe == "|": yl+=1#down move to [2][1]
    elif pipe == "J": yl,xl = yl+1, xl-1 #leftDown move to [2][0]
    elif pipe == "L": yl,xl = yl+1, xl+1 #leftUp move to [2][2]
    if y1==0 and x1==0: y1,x1 = yl, xl
    else: y2,x2 = yl, xl
  
  return (y1,x1,y2,x2)

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



def connect (neigh):
  centre = neigh[1][1] if neigh[1][1]!="S" else "7"
  #check these connections first
  left = neigh[1][0] if centre == "-" or centre == "J" or centre == "7" else None
  right = neigh[1][2]  if centre == "-" or centre == "J" or centre == "7" else None
  up = neigh[0][1] if centre == "|" or centre == "F" or centre == "7" else None
  down = neigh[2][1] if centre = "|" or centre == "L" or centre == "J" else None"
  #connected = np.array([[None,None,None], [None,None,None], [None,None,None]])
  left = True if left=="-" or left=="F" or left=="L" else False
  right = True if right=="-" or right=="7" or right=="J" else False
  up = True if up=="|" or up=="F" or up=="7" else False
  down = True if down=="|" or down=="L" or down=="J" else False
  connected = np.array([[None, up, None], [left, None, right,], [None, down, None]])
  return (connected)
  

#initialising
tiles = readFile2Data()
r, c = tiles.shape
print(r, c)

y, x = np.where(tiles == "S")
y,x=y[0],x[0]
print(y,x)
step=0

#start while true loop here
#getting data through functions
neigh = get_neigh(tiles[y,x],y,x) if check_bounds(y,x,r,c) else None
print(neigh)
y1,x1,y2,x2 = get_move(neigh)
y1,x1,y2,x2 = y+y1, x+x1, y+y2, x+x2
path1, path2= np.array([y1,x1]), np.array([y2,x2])
step+=1 #moved one step
print(y1,x1,y2,x2)
print(f"path1 = {path1}, path2 = {path2}")
z = input("enter a key: ")

print(check_bounds(y1,x1,r,c))

neigh = get_neigh(tiles[y1,x1],y1,x1) if check_bounds(y1,x1,r,c) else None
print(neigh)
z = input("enter a key: ")
