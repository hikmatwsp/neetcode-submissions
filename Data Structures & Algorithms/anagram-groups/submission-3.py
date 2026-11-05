class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedwords = {}
        for word in strs:
            sortedwords["".join(sorted(word))]= []
        
        for j in strs:
            sortedwords["".join(sorted(j))].append(j)

        return list(sortedwords.values())