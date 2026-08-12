class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        numFleets = 0

        positionSpeed = [[position[i], speed[i]] for i in range(n)]
        sortedPositionSpeed = sorted(positionSpeed, key = lambda pair: pair[0])
        sortedTime = [(target - sortedPositionSpeed[carIndex][0]) / sortedPositionSpeed[carIndex][1] for carIndex in range(n)]

        # these input test cases are sortedTime lists
        # test case: [1, 2, 3] => 1 fleet
        # test case: [3, 2, 1] => 3 fleets
        # test case: [4, 7, 4, 7] => 1 fleet
        # test case: [4, 7, 3, 6] => 2 fleets
        # test case: [5, 4, 6, 7] => 1 fleet

        # holds the time to reach target for the leading car of each fleet
        stack = []

        for carIndex in range(n - 1, -1, -1):
            carTime = sortedTime[carIndex]
            
            if len(stack) == 0 or carTime > stack[-1]:
                stack.append(carTime)
                numFleets += 1
        
        return numFleets
            
