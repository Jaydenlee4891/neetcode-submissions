class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        # Sort unique keys by their frequency count in descending order
        sorted_unique = sorted(count.keys(), key=count.get, reverse=True)
        return sorted_unique[:k]