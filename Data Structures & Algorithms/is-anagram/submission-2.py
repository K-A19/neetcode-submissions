class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if (len(s) != len(t)):
            return False

        s_sort = sorted(list(s))
        t_sort = sorted(list(t))

        for i in range(len(s)):
            if s_sort[i] != t_sort[i]:
                return False
        
        return True