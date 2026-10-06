class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        taskCounter = {}
        for task in tasks:
            if task not in taskCounter:
                taskCounter[task] = 1
            else:
                taskCounter[task] += 1

        maxHeap = list(taskCounter.values())
        heapq.heapify_max(maxHeap)
        queue = deque()
        time = 0

        while queue or maxHeap:
            time += 1
            if maxHeap:
                count = heapq.heappop_max(maxHeap)
                newCount = count - 1
                if newCount > 0:
                    queue.append([newCount, time + n])
                
            if queue and queue[0][1] == time:
                heapq.heappush_max(maxHeap, queue.popleft()[0])

        return time

                