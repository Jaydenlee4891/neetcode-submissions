class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        out = []

        for i,a in enumerate(nums):
            if a>0 :
                break
            if i>0 and a == nums[i-1]:
                continue
            
            l,r = i+1,len(nums)-1

            while l<r:
                target = a +nums[l] + nums[r]
                if target >0:
                    r -=1
                elif target <0:
                    l+=1
                else:
                    out.append([a,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and [a,nums[l],nums[r]] in out:
                        l+=1


        return out