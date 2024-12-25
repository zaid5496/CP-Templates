n=100
prime=[True for i in range(n+1)]
p=2
while p*p<=n:
    if prime[p]==True:
        for i in range(p*p,n+1,p):
            prime[i]=False
    p+=1
isPrime=[]
for i in range(2,len(prime)):
    if prime[i]==True:
        isPrime.append(i)
print(isPrime)