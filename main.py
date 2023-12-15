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


def check_bounds(y,x, r, c):
  if y+1>=r  or y-1<0 or x+1>=c or x-1<0 : return False
  else: return True


def get_neigh(el,y,x):
  neigh=np.array([[tiles[y-1][x-1],tiles[y-1][x],tiles[y-1][x+1]], [tiles[y][x-1],tiles[y][x],tiles[y][x+1]], [tiles[y+1][x-1],tiles[y+1][x],tiles[y+1][x]]])
  return neigh

def get_move(neigh):
  
  
  moveL, moveR = -1, +1 if "-": else 0, 0
  moveU, moveD = -1, +1 if "|": else 0, 0
  #moveU, moveL = 1, -1 if "L": else 0, 0
    
    

tiles = readFile2Data()
r, c = tiles.shape
print(r, c)

y, x = np.where(tiles == "S")
y,x=y[0],x[0]
print(x, y)


neigh = get_neigh(tiles[y,x],y,x) if check_bounds(y,x,r,c) else None
print(neigh)
