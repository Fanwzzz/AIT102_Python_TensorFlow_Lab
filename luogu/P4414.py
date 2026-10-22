nums = sorted(map(int, input().split()))
order = input().strip()
print(*(nums[ord(ch)-ord("A")] for ch in order))