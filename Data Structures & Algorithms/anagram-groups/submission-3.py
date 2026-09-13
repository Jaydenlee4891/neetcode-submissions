class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for word in strs:
            sort_word = "".join(sorted(word))
            seen[sort_word].append(word)
        return list(seen.values())
            
