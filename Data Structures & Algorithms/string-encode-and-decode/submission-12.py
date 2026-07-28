# neet#code -> neet code
# n#eet -> n eet wrong
# 4neet4code -> neet code
# ne4eet -> error 
# 4#neet 
# n3#eet


class Solution:

    def encode(self, strs: List[str]) -> str:
        enStr = ""
        for st in strs:
            enStr =  enStr+str(len(st))+"#"+st
        print(enStr)
        return enStr

    def decode(self, s: str) -> List[str]:
        ptr = 0
        res = []
        while ptr!=len(s):
            indexOfhash = s[ptr:].find('#')
            print(indexOfhash)
            lenOfS = int(s[ptr:ptr+indexOfhash])
            resS = s[ptr+indexOfhash+1: ptr+indexOfhash+1+lenOfS]
            print(resS)
            res.append(resS)
            ptr = ptr+indexOfhash+1+lenOfS
            print(ptr)
        return res
        
