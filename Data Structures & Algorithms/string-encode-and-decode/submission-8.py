class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        out = '00/'+'00/'.join(strs)+'00/'
        print(out)
        return out
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        ar = s.split("00/")
        ar.pop(0)
        ar.pop(-1)
        
        return ar