class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0 for _ in range(n)]

        # stack is a stack of indices of days whose next hottest day 
        # still needs to be determined
        stack = []

        for dayIndex in range(n):
            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[dayIndex]:
                otherDayIndex = stack.pop()
                result[otherDayIndex] = dayIndex - otherDayIndex
            
            stack.append(dayIndex)
        
        return result