class Solution:
    def romanToInt(self, s: str) -> int:
        nilai : dict[str, int] = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        total : int = 0
        for i in range(len(s)) :
            if i + 1 < len(s) and nilai[s[i]] < nilai[s[i + 1]] :
                total -= nilai[s[i]]
            else : 
                total += nilai[s[i]]
        return total