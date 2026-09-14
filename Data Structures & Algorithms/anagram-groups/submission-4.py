class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen=defaultdict(list)
        for word in strs:
            swor = "".join(sorted(word))
            seen[swor].append(word)
        return list(seen.values())
        