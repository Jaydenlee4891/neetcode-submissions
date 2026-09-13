class Solution:

    def encode(self, strs: List[str]) -> str:
        new_string = ""
        for word in strs:
            lenstr = len(word)
            new_string += str(lenstr) + "#" + word
        return new_string

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            # 2. Extract the length number (everything between i and j)
            length = int(s[i:j])
            # 3. Extract the word using the length
            # The word starts right after '#' (which is j + 1) 
            # and ends at (j + 1 + length)
            word = s[j + 1 : j + 1 + length]
            out.append(word)
            # 4. Move our pointer 'i' past this word to the next encoded chunk
            i = j + 1 + length
        return out