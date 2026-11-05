class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
     acuan : str = strs[0]   
     for i , huruf in enumerate(acuan) :
        for s in strs[1:] :
            if i == len(s) or s[i] != huruf :
                return acuan[:i]
     return acuan
        