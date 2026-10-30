## Lab 5

### Ex 1
```python
def oddsum(n):
    ls = []
    for i in range(1, n + 1, 2):
        ls.append(i)
    expression = " + ".join(str(i) for i in ls)
    return f"Output: {expression} = {sum(ls)}"

n = int(input("Enter a positive odd integer: "))
if n%2 == 0 or n <= 0:
    print("Invalid input!")
else:
    print(oddsum(n))
```

```bash
$ python ex1.py
Enter a positive odd integer: 5
Output: 5 + 3 + 1 = 9
```

### Ex 2
```python
def sum_and_product(nums):
    total = 0
    product = 1
    for i in nums:
        total += i
        product *= i
    return total, product

nums = list(map(int, input("Enter integers: ").split()))
total, product = sum_and_product(nums)
print("Sum:", total)
print("Product:", product)
```

```bash
$ python ex2.py
Enter integers: 1 2 3
Sum: 6
Product: 6
```

### Ex 3
```python
def reverse_string(s):
    return s[::-1]

sample_str = "ab1234abcd"
print(reverse_string(sample_str))
```

```bash
$ python ex3.py
dcba4321ba
```

### Ex 4
```python
def unique_list(ls):
    result = []
    for i in ls:
        if i not in result:
            result.append(i)
    return result

ls = list(map(int, input("Enter integers: ").split()))
print("Unique List:", unique_list(ls))
```

```bash
$ python ex4.py
Enter integers: 1 2 3 3 3 3 4 5
Unique List: [1, 2, 3, 4, 5]
```

### Ex 5
```python
def func(b, c, a=0):
    if a == 0:
        return a + b + c
    elif a == 1:
        return a * b * c
    else:
        print("Error: a must be 0 or 1!")
        return 0

print("Default(Sum):", func(2, 3))
print("Product:", func(2, 3, a=1))
print("Invalid mode result:", func(2, 3, a=2))
```

```bash
$ python ex5.py
Default(Sum): 5
Product: 6
Error: a must be 0 or 1!
Invalid mode result: 0
```

### Ex 6
```python
def calculate_stats(*args):
    if not args:
        return 0, 0, 0
    count = len(args)
    total = sum(args)
    return count, total, total / count

print(calculate_stats(1, 2, 3, 4))
print(calculate_stats())
```

```bash
$ python ex6.py
(4, 10, 2.5)
(0, 0, 0)
```