import socket # for socket
import sys
import time
 
def findWord(field, word):
    found = False
    while not found:
        for i in range(len(field)):
            for j in range(len(field[0])):
                if field[i][j] == word[0]:
                    for k in directions: # Try all directions
                        if i + k[0] < 0 or j + k[1] < 0 or i + k[0] >= len(field) or j + k[1] >= len(field):
                            continue
                        #print(word,i+k[0], j+k[1])
                        if field[i+k[0]][j+k[1]] == word[1]:
                            n = 1
                            while not found and field[i+k[0]*n][j+k[1]*n] == word[n]:
                                #print(word,i+k[0]*n, j+k[1]*n, n)
                                n += 1
                                if n == len(word):
                                    found = True
                                if i + k[0]*n < 0 or j + k[1]*n < 0 or i + k[0]*n >= len(field) or j + k[1]*n >= len(field):
                                    break
                        if found:
                            output = (i, j, k[0], k[1], len(word))
                            return output
                    
                        
def makeMask(field, word):                    
    mask = []
    for i in range(len(mat)):
        blep = []
        for j in range(len(mat)):
            blep.append(0)
        mask.append(blep)


    data = findWord(field, word)

    i = data[0]
    j = data[1]
    for r in range(data[4]):
        mask[i][j] = 1
        #print(i, j)
        i += data[2]
        j += data[3]
    return mask


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# default port for socket
port = 2000
host_ip = "127.0.0.1" 
 
# connecting to the server
s.connect((host_ip, port))
d = s.recv(4096) 
data = d.decode('utf-8')
print(data)
#d = s.recv(4096) 
#data = d.decode('utf-8')

if False:
    key = "ABC"
    s.sendall(key.encode('utf-8'))
    d = s.recv(4096) 
    data = d.decode('utf-8')
    print(data)
    exit()

lines = data.split("\n")
#print(data)
#print(lines)

mat = lines[:20]
words = lines[21:21+20]

for i in range(len(mat)):
    mat[i] = mat[i].split(" ")

mask = []
for i in range(len(mat)):
    blep = []
    for j in range(len(mat)):
        blep.append(0)
    mask.append(blep)


directions = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0),(-1,1)]

masks = []
for w in words:
    masks.append(makeMask(mat, w))

#for m in masks:
#    for i in range(len(mat)):
#        for j in range(len(mat)):
#            if m[i][j] == 1:
#                print(mat[i][j],end="")
#            else:
#                print("#",end="")
#        print()
#
#m = makeMask(mat, words[0])

#mask
for m in masks:
    for i in range(len(m)):
        for j in range(len(m[0])):
            mask[i][j] |= m[i][j]
debug = True
key = ""
for i in range(len(mat)):
    for j in range(len(mat)):
        if mask[i][j] == 0:
            if debug:
                print(mat[i][j],end="")
            key += mat[i][j]
        else:
            if debug:
                print("#",end="")
    if debug:
        print()

if debug:
    print()

#time.sleep(1)
s.sendall(key.encode('utf-8'))
d = s.recv(4096) 
data = d.decode('utf-8')
print(data)
print(key)
