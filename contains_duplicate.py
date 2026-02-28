class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        e = set()
        for n in nums:
            if n in e:
                return true
            e.add(n)

        return false
