class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        answer =[]
        out = False
        for i in nums:
            if i  not in answer:
                answer.append(i)
            else:
                out = True
        return out
