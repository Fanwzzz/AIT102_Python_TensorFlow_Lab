k = int(input())

m = 0

while (m+1)*(m+2)//2 < k:
    m += 1

print(m*(m+1)*(2*m+1)//6 + (k-(m*(m+1)//2))*(m+1))