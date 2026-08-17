class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                # لو وصل للحد الأقصى لكلمة قصيرة أو الحرف اختلف
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
            
        return res