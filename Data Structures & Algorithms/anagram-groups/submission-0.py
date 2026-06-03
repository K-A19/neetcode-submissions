class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        anagrams = []
        group_count = 0
        for string in strs:
            sorted_str = str(sorted(list(string)))
            if sorted_str in groups:
                anagrams[groups[sorted_str]].append(string)
            else:
                groups[sorted_str] = group_count
                group_count += 1
                anagrams.append([string])

        return anagrams
