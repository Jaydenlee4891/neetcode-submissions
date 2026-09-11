class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        current = []
        output = False
        for num in nums:
            if num not in current:
                current.append(num)
            else:
                output = True
        return output