# alg111a
Algorithm Course Samples
## HW 1 Integer Programming
```
5ₓ₁ +7ₓ₂ +9ₓ₃ +2ₓ₄ +1ₓ₅ ≤ 250
18ₓ₁ +4ₓ₂ -9ₓ₃ +10ₓ₄ +12ₓ₅ ≤ 285
4ₓ₁ +7ₓ₂ +3ₓ₃ +8ₓ₄ +5ₓ₅ ≤ 211
5ₓ₁ +13ₓ₂ +16ₓ₃ +3ₓ₄ -7ₓ₅ ≤ 315
```
### climbing
```
import random
max_num = 5
h = 1

coefs = [[5, 7, 9, 2, 1],
        [18, 4, -9, 10, 12],
        [4, 7, 3, 8, 5],
        [5, 13, 15, 3, -7]]

maxs = [250,  285, 211, 315]

num = [7, 8, 2, 9, 6]

current_answer = [0, 0, 0, 0, 0]
current_temp1 = [0, 0, 0, 0, 0]
current_temp2 = [0, 0, 0, 0, 0]

answer = [0, 0, 0, 0, 0]

# main
def Climbing():
    failCount = 0
    while failCount < 100:
        dh = random.randint(0,h)
        for i in range(max_num):
            current_temp1[i] += dh
            current_temp2[i] -= dh
            a = Count(current_temp1)
            b = Count(current_temp2)
            if a >= b:
                for j in range(max_num):
                    current_answer[j] = current_temp1[j]
            else:
                for j in range(max_num):
                    current_answer[j] = current_temp2[j]

            if limit(current_answer) == False:
                failCount += 1
            elif limit(current_answer) == True:
                Move()
                failCount = 0
    print(answer, Count(answer))
            
# move
def Move():
    for i in range(max_num):
        answer[i] = current_answer[i]
        current_temp1[i] = current_answer[i]
        current_temp2[i] = current_answer[i]

# Count max/min
def Count(a):
    temp = 0
    for i in range(max_num):
        temp = temp + a[i]*num[i]
    return temp

# limit
def limit(t):
    temp = 0
    for i in coefs:
        a = limitCount(i, t)
        if a > maxs[temp]:
            return False
        temp += 1
    return True

# limitcount
def limitCount(a, b):
    temp = 0
    for i in range(max_num):
        temp = temp + a[i]*b[i]
    return temp

Climbing()
```

![Result](https://github.com/cyncyn23/alg111a/tree/main/hw/integer.jpg)
