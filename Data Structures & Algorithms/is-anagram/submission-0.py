class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sarr = list(s)
        tarr = list(t)

        sarr.sort()
        tarr.sort()

        if sarr == tarr:
            return True
        return False
