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
        # print(dic)
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
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ar = []
        markedAr = [0] * len(strs)

        for i in range(len(strs)):
            if markedAr[i] == 1:
                continue
            temp =[strs[i]]
            markedAr[i] = 1
            for j in range(len(strs)):
                if i==j:
                    continue
                if markedAr[j]==0 and self.isAnagram(strs[i], strs[j]):
                    temp.append(strs[j])
                    markedAr[j]=1
            ar.append(temp)
        return ar
            