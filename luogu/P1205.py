def reflect(pattern):
    return [line[::-1] for line in pattern]

def rotate(pattern):
    return ["".join(col) for col in zip(*pattern[::-1])]

def classify(orignal, target):
    
    current = orignal
    for i in range(1,4):
        current = rotate(current)
        if current == target:
            return i

    mirrored = reflect(orignal)
    if mirrored == target:
        return 4

    current = mirrored
    for _ in range(1,4):
        current = rotate(current)
        if current == target:
            return 5

    if orignal == target:
        return 6

    return 7

n = int(input())

orignal = [input() for _ in range(n)]
target = [input() for _ in range(n)]

print(classify(orignal, target))