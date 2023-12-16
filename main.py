import numpy as np
from itertools import combinations

def readFile2Data():
  f=open("day11_input.txt", "r")
  """  image=np.array(f.read().strip().splitlines())
  print(image.shape)
  print(image)
  z= input("enter a key: ")
  for line in image:
    row= [c for c in line]
    print(row)
    z= input("enter a key: ")"""
  image=np.array([])
  count=0
  for line in f:
    line=line.strip().split()
    for i in line:
      row = [c for c in i]
      row.insert(0, ".")
      row.append(".")
      image = np.r_[image, row]
      #tiles = np.append(tiles,tile_row) #does the same too
      #print(row)
      #z= input("enter a key: ")
      count+=1
  length = len(row)
  #print(f"count = {count} and length = {length}")
  #z= input("enter a key: ")
  #z= input("enter a key: ")
  row = ["." for c in range(length)]
  image = np.insert(image, 0, row, axis=0 )
  image = np.append(image, row)
  #print(image.shape)
  image = image.reshape(count+2, length)
  #print(image.shape)
  #z= input("enter a key: ")
  f.close
  return image
  
image = np.array(readFile2Data())
#print(image.shape)

gal_wh = np.where(image == "#")
#print(len(gal_wh))
#print(gal_wh[0])
#print(len(gal_wh[0]))
#print(len(gal_wh[1]))

galaxies = np.array([[(gal_wh[0][i], gal_wh[1][i])] for i in range(len(gal_wh[0]))])
print(galaxies.shape)
print(f"{galaxies[0][0][0]}, {galaxies[0][0][1]}")
print(len(galaxies))
"""for i in galaxies:
  print(i)
  print(f"{i[0][0]}, {i[0][1]}")
  z= input("enter a key: ")"""

ids = np.array([i for i in range(len(galaxies))])
#print(ids)
print(ids.shape)
print(len(ids))


