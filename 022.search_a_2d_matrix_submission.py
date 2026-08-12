class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])

        # first find which list in the matrix can have the solution
        # then search that list for the solution

        lowerListIndex = 0
        upperListIndex = m - 1

        while lowerListIndex <= upperListIndex:
            midListIndex = (lowerListIndex + upperListIndex) // 2

            if matrix[midListIndex][0] > target:
                # target can only be in list left of midListIndex
                upperListIndex = midListIndex - 1
            
            elif matrix[midListIndex][-1] < target:
                # target can only be in list right of midListIndex
                lowerListIndex = midListIndex + 1
            
            # target can only be in this list
            else: # matrix[midListIndex][0] <= target and matrix[midListIndex][-1] >= target:
                lowerBound = 0
                upperBound = n - 1

                while lowerBound <= upperBound:
                    midIndex = (lowerBound + upperBound) // 2
                    
                    if matrix[midListIndex][midIndex] > target:
                        # target can only be left of midIndex
                        upperBound = midIndex - 1
                    
                    elif matrix[midListIndex][midIndex] < target:
                        # target can only be right of midIndex
                        lowerBound = midIndex + 1
                    
                    else: # matrix[midListIndex][midIndex] == target:
                        return True 
                
                return False
        return False

