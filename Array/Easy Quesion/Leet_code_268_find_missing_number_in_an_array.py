# find numbers 
nums = [1,2,4,5,6,7]
n = len(nums)

for i in range (i, n+1):
    if i not in nums:
        return i
"""
time complexity is o(N^2)
space complexity is o (N)
"""
# potimal solution 
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        m = n * (n + 1) // 2
        a = sum(nums)

        return m - a
    
    """
    time complexity is o(N)
    space complexity is o(N)
    """