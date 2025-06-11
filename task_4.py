n = int(input())
nums = list(map(int, input().split()))

suffix_max = [0] * (n + 1)
suffix_max[n] = -1
for i in range(n - 1, -1, -1):
    suffix_max[i] = max(nums[i], suffix_max[i + 1])

prefix_min = 10**10
res = 0

for k in range(1, n):
    prefix_min = min(prefix_min, nums[k - 1])
    if prefix_min >= suffix_max[k]:
        res = k

print(res)
