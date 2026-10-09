class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if len(tasks) == 0:
            return 0
        

        countDict = Counter(tasks)
        maxHeap = list(countDict.values())
        heapq.heapify_max(maxHeap)
        queue = deque()
        timer = 0

        while maxHeap or queue:
            timer += 1

            if maxHeap:
                count = heapq.heappop_max(maxHeap)
                newCount = count - 1
                if newCount > 0:
                    queue.append([newCount, timer + n])
            if queue and queue[0][1] == timer:
                node = queue.popleft()[0]
                heapq.heappush_max(maxHeap, node)
        
        return timer