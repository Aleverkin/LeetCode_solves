# 1
# 11
# 112
# 1234
# -3-31
# -3-21

ind = 0
prev = -1000
while ind < len(nums):
    if nums[ind] == prev:
        nums.pop(ind)
    else:
        prev = nums[ind]
        ind += 1