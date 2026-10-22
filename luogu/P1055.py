ISBN = input().split("-")
digits = ISBN[0]+ISBN[1]+ISBN[2]
rec = 0
for i in range(9):
    rec += int(digits[i]) * (i+1)
rec %= 11
check = "X" if rec==10 else str(rec)
if check == ISBN[3]:
    print("Right")
else:
    print(ISBN[0],ISBN[1],ISBN[2],check,sep="-")