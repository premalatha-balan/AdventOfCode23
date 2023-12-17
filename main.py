import numpy as np
from itertools import combinations
import math

def readFile2Data():
  f=open("testdata2day11.txt", "r")
  image=np.array([])
  count=0
  for line in f:
    line=line.strip().split()
    for i in line:
      row = [c for c in i]
      #row.insert(0, ".")
      #row.append(".")
      image = np.r_[image, row]
      #tiles = np.append(tiles,tile_row) #does the same too
      #print(row)
      #z= input("enter a key: ")
      count+=1
  length = len(row)
  #print(f"count = {count} and length = {length}")
  #z= input("enter a key: ")
  #z= input("enter a key: ")
  #row = ["." for c in range(length)]
  #image = np.insert(image, 0, row, axis=0 )
  #image = np.append(image, row)
  #print(image.shape)
  image = image.reshape(count, length)
  #print(image.shape)
  #print(image)
  #z= input("enter a key: ")
  f.close
  return image

def dist_pair(pair):
  gal1 = galaxies[pair[0]][0]
  gal2 = galaxies[pair[1]][0]
  #print(gal1, gal2)
  dist = abs(gal1[0]-gal2[0])+abs(gal1[1]-gal2[1])
  print(f"gal1 = {gal1}, gal2 = {gal2} and  dist = {dist}")
  #z= input("enter a key: ")
  return abs(gal1[0]-gal2[0])+abs(gal1[1]-gal2[1])
  
  
image = np.array(readFile2Data())
#print(image.shape)
r,c = image.shape

#getting all the galaxies
gal_wh = np.where(image == "#")
#print(len(gal_wh))
#print(f"length of gal_wh[0] = {len(gal_wh[0])}")
#print(f"length of gal_wh[1] = {len(gal_wh[1])}")
print(f"gal_wh[0] before expanding {gal_wh[0]}")
#print(f"gal_wh[1] before expanding {gal_wh[1]}")
#print(len(gal_wh[1]))
#z= input("enter a key at checking: ")

"""#checking the rows where there are no galaxies so that we can expand that row
row_insert = ["." for i in range(c)]
count=0
for i in range(r):
  if i not in gal_wh[0]:
    print(f"row {i} is not a galaxy")
    image = np.insert(image, i+count, row_insert, axis=0)
    count+=1

print(f"added {count} rows")
#print(f"after expanding rows, image shape is {image.shape} ")
#z= input(f"enter a key after expanding rows: {r+count} ")
r,c = image.shape

#expanding columns
column_insert = ["." for i in range(r)]
count=0
for i in range(c):
  if i not in gal_wh[1]:
    print(f"column {i} is not a galaxy")
    image = np.insert(image, i+count, column_insert, axis=1)
    count+=1

print(f"added {count} columns")

r,c = image.shape"""
#print(f"after expanding rows, image shape is {image.shape} ")
#z= input(f"enter a key after expanding columns: ")

#print(f"image =/n/n {image}")

"""#finding the galaxies new locations after the expansion
#getting all the galaxies
gal_wh = np.where(image == "#")
#print(len(gal_wh))
print(f"\n\nafter expanding")
#print(f"length of gal_wh[0] = {len(gal_wh[0])}")
#print(f"length of gal_wh[1] = {len(gal_wh[1])}")
print(f"gal_wh[0] after expanding {gal_wh[0]}")
print(f"gal_wh[1] after expanding {gal_wh[1]}")
#print(len(gal_wh[1]))
#z= input("enter a key at checking: ")


galaxies = np.array([[(gal_wh[0][i], gal_wh[1][i])] for i in range(len(gal_wh[0]))])
#print(galaxies.shape)
#print(f"{galaxies[0][0][0]}, {galaxies[0][0][1]}")
#print(len(galaxies))"""

#expanding 10 times
expand=0
count=0
times=1
#print("\n\nworking on rows")
for i in range(r):
  if i not in gal_wh[0]:
    #print(f"row {i} is not a galaxy")
    #image = np.insert(image, i+count, row_insert, axis=0)
    expand+=times
    #z= input("enter a key: ")
    #gal_wh[0] = np.insert(gal_wh[0], (gal_wh[0].index[i]) )
    count+=1
  elif count!=0:
    loc = list(np.where(gal_wh[0]==i))
    for l in range(len(loc)):
      print(f"changing {gal_wh[0][loc[l]]} to {gal_wh[0][loc[l]]+expand}")
      gal_wh[0][loc[l]] = gal_wh[0][loc[l]]+expand
      print(f"changed {gal_wh[0][loc[l]]}")
      #z= input("enter a key: ")

print(f"after expanding rows, gal_wh[0] is {gal_wh[0]}")
#z= input("enter a key: ")
#print(f"added {count} rows")


count=0
expand=0
times=1
#print("\n\nworking on columns")
print(f"gal_wh[1] before expanding {gal_wh[1]}")
for i in range(c):
  if i not in gal_wh[1]:
    #print(f"column {i} is not a galaxy")
    #image = np.insert(image, i+count, row_insert, axis=0)
    expand+=times
    #print(f"expand = {expand} and count = {count}")
    #z= input("enter a key: ")
    #gal_wh[0] = np.insert(gal_wh[0], (gal_wh[0].index[i]) )
    count+=1
  elif count!=0:
    loc = list(np.where(gal_wh[1]==i))
    for l in range(len(loc)):
      #print(f"changing {gal_wh[1][loc[l]]} to {gal_wh[1][loc[l]]+expand}")
      gal_wh[1][loc[l]] = gal_wh[1][loc[l]]+expand
      #print(f"changed {gal_wh[1][loc[l]]}")
      #print(f"expand = {expand} and count = {count}")
      #z= input("enter a key: ")

print(f"after expanding columns, gal_wh[1] is {gal_wh[1]}")
#z= input("enter a key: ")

#creating the galaxies pairs after expanding
galaxies = np.array([[(gal_wh[0][i], gal_wh[1][i])] for i in range(len(gal_wh[0]))])
#print(galaxies.shape)
#print(f"{galaxies[0][0][0]}, {galaxies[0][0][1]}")
#print(len(galaxies))
#print(galaxies)

#creating the combination of pairs with their ids
ids = np.array([i for i in range(len(gal_wh[0]))])
pairs = list(combinations(ids, 2))

sum_lst = list(map(dist_pair, pairs))
sum_lst.sort()
print(f"sume of distances = {(sum_lst)}")
print(f"sum = {sum(sum_lst)}")

