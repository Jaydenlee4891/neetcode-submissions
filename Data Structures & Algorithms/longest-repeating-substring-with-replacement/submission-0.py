class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        longest = 0
        l = 0
        max_freq = 0
        for r in range(len(s)):
            # Add the current character to our frequency map
            count[s[r]] = count.get(s[r], 0) + 1
            # Keep track of the highest frequency seen in any valid window so far
            max_freq = max(max_freq, count[s[r]])
            # If characters to replace exceed k, shrink the window from the left
            if (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1
            # Update the maximum length found
            longest = max(longest, r - l + 1)
        return longest