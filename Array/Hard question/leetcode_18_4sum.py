class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums) 
        ans = []
        nums.sort()
        for i in range(0 , n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1 , n):    
                if j > i +1 and nums[j] == nums[j-1]:
                    continue
                k = j +1
                l = n -1

                while k < l:
                    total = nums[i] + nums[j]   + nums[k]+ nums[l]
                    if total == target:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        k +=1
                        l -=1
                        while k <1 and numd[k] == nums[k-1]:
                            k+=1
                        while l > k and nums[l] == nums[l+1]:
                            l -=1
                    elif total < target:
                            k +=1
                    else:
                            l -=1 

        return ans                  
                      




"""
the time complexity is o(n3)
space complexity is no of ans  o(1)
"""
