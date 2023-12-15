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

tiles = readFile2Data()
#print(len(tiles))
print(tiles.shape)
#print(tiles)
#print(tiles[-1])

