def combine(self, n, k):
    res = []
    comb = list(range(1, k + 1))
    res.append(comb[:])
        
    while True:
        for i in reversed(range(k)):
            if comb[i] != n - k + 1 + i:
                break
        else:
            break
        
        comb[i] += 1
        for j in range(i + 1, k):
            comb[j] = comb[j - 1] + 1
        
        res.append(comb[:])
   
    return res