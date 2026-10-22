n = int(input())
m1 = list(map(int, input().split()))
m2 = list(map(int, input().split()))
m3 = list(map(int, input().split()))
c1 = ((n+m1[0]-1)//m1[0])*m1[1]
c2 = ((n+m2[0]-1)//m2[0])*m2[1]
c3 = ((n+m3[0]-1)//m3[0])*m3[1]
print(min([c1,c2,c3]))