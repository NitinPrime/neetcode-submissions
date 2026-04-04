class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = sorted(set(nums))

        longest = 1
        count = 1

        for i in range(1, len(n)):
            if n[i] == n[i-1] + 1:
                count += 1
            else:
                count = 1
            
            longest = max(longest, count)
        return longest