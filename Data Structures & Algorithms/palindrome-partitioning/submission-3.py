class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(subset, substr):
            print(subset, substr)
            if substr == "":
                res.append(subset.copy())
            for i in range(0, len(substr)):
                if substr[:i+1] == substr[:i+1][::-1]:
                    subset.append(substr[:i+1])
                    dfs(subset, substr[i+1:])
                    subset.pop()
        dfs([], s)
        return res
          