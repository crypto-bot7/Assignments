def solve(n):
    if n<4:
        return str(2**(n-1))+'/'+str(2**n)
    A=2
    AA=1
    AAA=1
    P = 4
    count = 8
    for i in range(4,n+1):
        temp= AAA
        AAA=AA
        AA=A
        A=P
        P= count
        count = (count-temp)*2+temp
    return str(AAA+AA+A)+'/'+str(count)

# n = int(input())
n=5
print(solve(n))
n=10
print(solve(n))