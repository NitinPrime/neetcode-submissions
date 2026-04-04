class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dit = defaultdict(int)

        for num in nums:
            dit[num] += 1

        sorted_nums = sorted(dit, key = lambda x: dit[x], reverse = True)
        
        return sorted_nums[:k]