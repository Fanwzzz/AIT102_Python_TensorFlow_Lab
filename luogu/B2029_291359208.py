h, r = map(int, input().split())
v = h*(3.14*(r**2))
print(int((20000.0+v-1.0)//v))