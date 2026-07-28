class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dic = {}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        print(dic)
        for j in t:
            if j not in dic:
                return False
            else:
                dic[j]-=1
        print(dic)


        for i in dic.values():
            if i != 0:
                return False
        return True