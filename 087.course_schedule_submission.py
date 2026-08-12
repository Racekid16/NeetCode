class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = dict()

        for course in range(numCourses):
            adjList[course] = []
        
        for prerequisite in prerequisites:
            a = prerequisite[0]
            b = prerequisite[1]
            adjList[a].append(b)
        
        visiting = set()
        
        # test case: 
        # 1 -> 2
        # 1 -> 3
        # 2 -> 4
        # 3 -> 4
        def canTake(course):
            if course in visiting:
                return False
            
            if len(adjList[course]) == 0:
                return True
            
            visiting.add(course)
            for prerequisite in adjList[course]:
                if not canTake(prerequisite):
                    return False
            
            adjList[course] = []
            visiting.remove(course)
            
            return True
        
        for course in range(numCourses):
            if not canTake(course):
                return False
        
        return True
        