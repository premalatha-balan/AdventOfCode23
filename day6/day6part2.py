#read this data from the file
#Time:        42     89     91     89
#Distance:   308   1170   1291   1467

t = 42899189
d = 308117012911467
getDist = 2*sum((t - i) * i > d for i in range(1, int(t / 2) + 1))
print(getDist)
