class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
            
        sorted_counts = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        
        return [item[0] for item in sorted_counts[:k]]