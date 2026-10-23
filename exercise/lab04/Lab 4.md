## Lab 4

### exercise 1

```python
n = int(input("Enter a positive odd integer: "))
while n <= 0 or n%2 == 0:
    n = int(input("Invalid input! Please enter a positive odd integer: "))

s = 0
print("Output: ", end="")
for i in range(1, n+1, 2):
    s += i
    if i == n:
        print(i, end="")
    else:
        print(i, end=" + ")
print(f" = {s}")
```

```bash
Output: 1 + 3 + 5 + 7 + 9 + 11 = 36
```

### exercise 2

```python
n = int(input("Please enter a positive integer: "))
while n <= 0:
    n = int(input("Invalid input! Please enter a positive integer: "))

i = n
digits = 0
while i > 0:
    digits += 1
    i = i // 10
print(f"The total number of digits in {n} is {digits}")

print("Collatz sequence: ", end="")
while n != 1:
    print(n, end=", ")
    if n%2 == 0:
        n = n // 2
    else:
        n = 3*n + 1
print(n)
```

```bash
The total number of digits in 15 is 2
Collatz sequence: 15, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1
```

**exercise 3**

```python
n = int(input("Please enter a positive integer: "))
while n <= 0:
    n = int(input("Invalid input! Please enter a positive integer: "))

for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
```

```bash
1 2 3 4 5 6 7 8 9 10 
1 2 3 4 5 6 7 8 9 
1 2 3 4 5 6 7 8 
1 2 3 4 5 6 7 
1 2 3 4 5 6 
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
```

### exercise 4

```python
n = int(input("Please enter a positive odd integer: "))
while n <= 0 or n%2 == 0:
    n = int(input("Invalid input! Please enter a positive odd integer: "))

for i in range(0, n+1, 2):
    print(" "*(i//2)+"*"*(n-i))
```

```bash
*******
 *****
  ***
   *
```

### exercise 5

```python
ls = list(map(int, input("Please enter a list of integers: ").split()))
ct = 0
print("Checking list:", ls)

for i in ls:
    if i < 0:
        print(f"Skipping negative value: {i}")
        continue
    if i%2 != 0:
        ct += 1
        print(f"Found odd number: {i}")
        if ct == 3:
            print("Found 3 odd numbers! Stopping search.")
            break

if ct < 3:
    print(f"The total number of odd numbers found is {ct}")
```

```bash
Checking list: [2, -5, 7, 4, 9, 11, 14, 15]
Skipping negative value: -5
Found odd number: 7
Found odd number: 9
Found odd number: 11
Found 3 odd numbers! Stopping search.
```

### exercise 6

```python
import time

while True:
    print("=== MENU ===")
    print("1. Generate Multiplication Table")
    print("2. Run Countdown")
    print("3. Exit")
    option = input("Select an option (1-3): ")

    if option == "1":
        k = int(input("Enter table number: "))
        m = int(input("Enter limit: "))
        while m <= 0:
            m = int(input("Invalid input! Please enter a positive limit: "))
        for num in range(1, m+1):
            print(f"{k} x {num} = {k*num}")
    elif option == "2":
        s = int(input("Enter starting number: "))
        while s <= 0:
            s = int(input("Invalid input! Please enter a positive starting number: "))
        for num in range(s, 0, -1):
            print(num)
            time.sleep(1)
    elif option == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid input. Please choose 1, 2 or 3.")
```

```bash
=== MENU ===
1. Generate Multiplication Table
2. Run Countdown
3. Exit
10
9
8
7
6
5
4
3
2
1
=== MENU ===
1. Generate Multiplication Table
2. Run Countdown
3. Exit
Goodbye!
```
