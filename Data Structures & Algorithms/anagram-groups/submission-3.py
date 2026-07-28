class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map ={}
        for string in strs:
            key = self.getKey(string)
            print(key)
            if key in map:
                map[key].append(string)
            else:
                map[key] = [string]
        return map.values()
	
    def getKey(self, tempStr: str) -> str:
        ar  = [0]*26
        for ch in tempStr:
            ar[ord(ch)-ord("a")]+=1
            
        return ",".join([str(num) for num in ar])
			

		
	
