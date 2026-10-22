m = sorted(map(int, input().split()))
if m[0]+m[1]>m[2]:
    if m[0]**2+m[1]**2==m[2]**2:
        print("Right triangle")
    elif m[0]**2+m[1]**2>=m[2]**2:
        print("Acute triangle")
    else:
        print("Obtuse triangle")
    if m[0]==m[1] or m[0]==m[2] or m[2]==m[1]: 
        print("Isosceles triangle") 
        if m[0]==m[1]==m[2]:
            print("Equilateral triangle")
else:
    print("Not triangle")    