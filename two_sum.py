class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        diff = {}

        for i, v in enumerate(nums):
            if target - v in diff:
                res.append(diff[target-v])
                res.append(i)

            diff[v] = i

        return res
