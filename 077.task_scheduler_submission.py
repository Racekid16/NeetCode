import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCounts = dict()
        for task in tasks:
            taskCounts[task] = taskCounts.get(task, 0) + 1

        # prioritize completing more frequent tasks first.
        maxHeap = [-taskCounts[task] for task in taskCounts]
        heapq.heapify(maxHeap)
        # keep track of task cooldowns.
        queue = deque()

        cycle = 0

        while len(maxHeap) > 0 or len(queue) > 0:
            while len(queue) > 0 and queue[0][1] <= cycle:
                heapq.heappush(maxHeap, queue.popleft()[0])

            if len(maxHeap) > 0:
                taskCount = heapq.heappop(maxHeap)
                taskCount += 1

                if taskCount < 0:
                    queue.append((taskCount, cycle + n + 1))
            
            cycle += 1
        
        return cycle
