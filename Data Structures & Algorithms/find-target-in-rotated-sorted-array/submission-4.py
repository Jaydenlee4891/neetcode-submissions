class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            # 1. Found the target!
            if nums[mid] == target:
                return mid
            
            # 2. Check if the left half is sorted
            if nums[l] <= nums[mid]:
                # Is the target safely inside the sorted left half?
                if nums[l] <= target < nums[mid]:
                    r = mid - 1  # Search left
                else:
                    l = mid + 1  # Search right
                    
            # 3. Otherwise, the right half must be sorted
            else:
                # Is the target safely inside the sorted right half?
                if nums[mid] < target <= nums[r]:
                    l = mid + 1  # Search right
                else:
                    r = mid - 1  # Search left
                    
        # If we loop through everything and find nothing
        return -1