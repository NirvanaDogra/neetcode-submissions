class Solution:
	def isAnagram(self, s: str, t:str) -> bool:
		map = {}
		for ch in s:
			if ch in map:
				map[ch]+=1
			else:
				map[ch] = 1
		print(map)
		for ch in t:
			if ch in map:
				map[ch]-=1
			else:
				return False
		print(map)
		for i in map.values():
			if i!=0:
				return False
		return True
	
