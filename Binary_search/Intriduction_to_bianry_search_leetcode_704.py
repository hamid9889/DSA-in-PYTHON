class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n-1
        while low<=high:
            mid = (low + high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid-1
        return -1                
        
        
        """
        the time complexity is O(log_base_2 N)
        space somplexity is o(1)
        
        """