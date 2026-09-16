class Solution:
    def isValid(self, s: str) -> bool:
        val = {")": "(", "]":"[","}":"{"}
        curr = []
        for i in s:
            if i in val:
                top_element = curr.pop() if curr else '#'
                if top_element !=val[i]:
                    return False
            else:
                curr.append(i)
        return not curr