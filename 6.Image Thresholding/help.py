H = image[:,:,0]
S = image[:,:,1]
V = image[:,:,2]

# you shold implement part a,b,c and in the last use following code

for i in range(result.shape[0]):
    for j in range(result.shape[1]):
        if result[i][j] == 0:
            #fig1[i][j] = 128
            H[i][j] = 0
            S[i][j] = 255
            V[i][j] = 0
        else:
            H[i][j] = 0
            S[i][j] = 0
            V[i][j] = 255
image[:,:,0] = H
image[:,:,1] = S
image[:,:,2] = V