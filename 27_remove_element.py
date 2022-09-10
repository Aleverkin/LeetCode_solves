nums = [1, 3, 2, 4, 3]
val = 3

i = 0
while i < len(nums):
    if nums[i] == val:
        nums.pop(i)
    else:
        i += 1

print(nums)


for _ in range(sum([1 for x in nums if x == val])):
    nums.remove(val)