class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = dict()

        for course in range(numCourses):
            adjList[course] = []
        
        for prerequisite in prerequisites:
            a = prerequisite[0]
            b = prerequisite[1]
            adjList[a].append(b)
        
        visiting = set()
        taken = set()
        ordering = []
        
        # test case: 
        # 1 -> 2
        # 1 -> 3
        # 2 -> 4
        # 3 -> 4
        def canTake(course):
            if course in visiting:
                return False
            
            if course in taken:
                return True
            
            visiting.add(course)
            for prerequisite in adjList[course]:
                if not canTake(prerequisite):
                    return False
            
            visiting.remove(course)
            taken.add(course)
            ordering.append(course)
            return True
        
        for course in range(numCourses):
            if not canTake(course):
                return []
        
        return ordering
        