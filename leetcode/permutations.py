from turtle import back


class Solution:
    def permute(self, nums):
        def backtrack(p=0):
            if p == length:
                output.append(nums[:])
                return
            for i in range(p, length):
                nums[i], nums[p] = nums[p], nums[i]
                backtrack(p + 1)
                nums[p], nums[i] = nums[i], nums[p]
        
        output = []
        length = len(nums)
        backtrack()
        return output
        
        

result = Solution().permute([1,2,3])
print(result)






















