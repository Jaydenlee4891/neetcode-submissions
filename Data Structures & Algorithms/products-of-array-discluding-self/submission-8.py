class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n =len(nums)
        out = [1]*n
        prev= 1
        for i in range(n):
            out[i] *= prev
            prev *= nums[i]
        prev= 1
        for i in range(n-1 , -1,-1):
            out[i] *= prev
            prev *= nums[i]
        return out            

