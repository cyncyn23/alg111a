import random
max_num = 5
h = 1

coefs = [[5, 7, 9, 2, 1],
        [18, 4, -9, 10, 12],
        [4, 7, 3, 8, 5],
        [5, 13, 15, 3, -7]]

maxs = [250,  285, 211, 315]

num = [7, 8, 2, 9, 6]

currentAns = [0, 0, 0, 0, 0]
currentT1 = [0, 0, 0, 0, 0]
currentT2 = [0, 0, 0, 0, 0]

answer = [0, 0, 0, 0, 0]

# 主程式
def Climbing():
    failCount = 0
    while failCount < 100:
        dh = random.randint(0,h)
        for i in range(max_num):
            currentT1[i] += dh
            currentT2[i] -= dh
            a = Count(currentT1)
            b = Count(currentT2)
            if a >= b:
                for j in range(max_num):
                    currentAns[j] = currentT1[j]
            else:
                for j in range(max_num):
                    currentAns[j] = currentT2[j]

            if limit(currentAns) == False:
                failCount += 1
            elif limit(currentAns) == True:
                Move()
                failCount = 0
    print(answer, Count(answer))
            
# Move
def Move():
    for i in range(max_num):
        answer[i] = currentAns[i]
        currentT1[i] = currentAns[i]
        currentT2[i] = currentAns[i]

# Count max/min
def Count(a):
    temp = 0
    for i in range(max_num):
        temp = temp + a[i]*num[i]
    return temp

# Limit
def limit(t):
    temp = 0
    for i in coefs:
        a = limitCount(i, t)
        if a > maxs[temp]:
            return False
        temp += 1
    return True

# limitCount
def limitCount(a, b):
    temp = 0
    for i in range(max_num):
        temp = temp + a[i]*b[i]
    return temp

Climbing()