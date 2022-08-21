class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        ans = None

        for i in range(n):
            for j in range(i, n):
                if nums[i] + nums[j] == target and i != j:
                    ans = [i, j]
                    break

            if ans != None:
                break

        return ans