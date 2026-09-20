class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev = 1
        out = [1]*len(nums)
        for i in range(len(nums)):
            out[i] *= prev
            prev *=nums[i]

        [1,1,2,8]
        nprev = 1
        for i in range(len(nums)-1,-1,-1):
            out[i] *= nprev
            nprev *= nums[i]
        return out
