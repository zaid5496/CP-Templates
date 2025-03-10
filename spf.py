def compute_spf(maxn):
    spf = list(range(maxn + 1))
    for i in range(2, int(maxn**0.5) + 1):
        if spf[i] == i:
            for j in range(i*i, maxn+1, i):
                if spf[j] == j:
                    spf[j] = i
                
    return spf
    
maxn = 10**6  # Example maximum limit for SPF computation
spf = compute_spf(maxn)

# To find the smallest prime factor of a number
number = 117
print(f"Smallest prime factor of {number} is {spf[number]}")
