from operator import add, sub, mul

rules = {"a": ("+", add), "b": ("-", sub), "c": ("*", mul)}

i = int(input())
operation = ""

for _ in range(i):
    fields = input().split()

    if len(fields) == 3:
        operation = fields[0]
        fields = fields[1:]

    x, y = map(int, fields)

    symbol, calculate = rules[operation]
    result = calculate(x, y)

    expression = f"{x}{symbol}{y}={result}"
    print(expression)
    print(len(expression)) # type: ignore