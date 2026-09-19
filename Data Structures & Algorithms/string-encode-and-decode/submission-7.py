class Solution:

    def encode(self, strs: List[str]) -> str:
        word = ""
        for s in strs:
            length = len(s)
            word += str(length) + "#" +s
        return word
    def decode(self, s: str) -> List[str]:
        i = 0
        out = []
        while i<len(s):
            j=i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            out.append(s[j+1:j+length+1])
            i = j+length+1
        return out
