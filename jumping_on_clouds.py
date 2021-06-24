def jumpingOnClouds(c):
    n = len(c)
    i = 0
    nmoves = 0
    while True:
        if (i+1 == n-1) or  c[i+2] == 1:
            step = 1
        else:
            step = 2
        i += step
        nmoves += 1
        if i+1 == n:
            return nmoves

path = [0, 0, 0, 1, 0, 0]
nmoves = jumpingOnClouds(path)
print(nmoves)