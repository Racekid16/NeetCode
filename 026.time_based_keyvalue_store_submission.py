class TimeMap:

    def __init__(self):
        self.timeMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        
        self.timeMap[key].append([timestamp, value])


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        
        latestValue = self.timeMap[key][-1]
        latestValueTime = latestValue[0]
        if timestamp >= latestValueTime:
            return latestValue[1]
        
        # binary search- find the value of target pair
        # which has the largest time stamp <= timestamp
        else:
            leftIndex = 0
            rightIndex = len(self.timeMap[key]) - 1

            targetVal = ""

            while leftIndex <= rightIndex:
                midIndex = (leftIndex + rightIndex) // 2

                midVal = self.timeMap[key][midIndex]

                if midVal[0] == timestamp:
                    return midVal[1]
                
                elif midVal[0] > timestamp:
                    # target must be to the left of midVal
                    rightIndex = midIndex - 1
                
                else:   # midVal[0] < timestamp
                    # midVal might be target,
                    # or target is to the right of midVal
                    targetVal = midVal[1]
                    leftIndex = midIndex + 1
            
            return targetVal



