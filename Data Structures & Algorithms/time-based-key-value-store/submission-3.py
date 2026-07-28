class TimeMap:

    def __init__(self):
        self.timeMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            self.timeMap[key] = self.timeMap[key] + [(value, timestamp)]
            
        else:
            self.timeMap[key] = [(value, timestamp)]
        
        print(self.timeMap)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        lst = self.timeMap[key]
        temp = ("", None)
        print(key, timestamp, lst)
        for el in lst:
            
            if el[1] == timestamp:
                return el[0]
            elif timestamp > el[1]:
                temp = el
            else:
                continue
        return temp[0]
                
            
