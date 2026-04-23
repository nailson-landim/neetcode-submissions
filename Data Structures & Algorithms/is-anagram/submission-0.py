class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If I sort the characters of both strings and they are the same it does work
        if sorted(s) == sorted(t):
            return True
        return False