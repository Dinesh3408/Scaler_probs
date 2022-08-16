class Solution:
    def twoSum(self, nums, target):
        seen = []
        for i in range(len(nums)):
            comp = target -nums[i]
            if comp not in seen:
                seen.append(comp)
            
            
        return comp , nums[i]
                
s = Solution()
print(s.twoSum([2,7,11,6], 13))
