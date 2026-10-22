h, r = map(int, input().split())
v = 314 * r**2 * h
print((2000000+v-1)//v)