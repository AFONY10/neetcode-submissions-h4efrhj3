class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        
        countDict = Counter(tasks)
        maxHeap = list(countDict.values())
        heapq.heapify_max(maxHeap)
        queue = deque()
        cycles = 0

        while maxHeap or queue:
            cycles += 1

            if maxHeap:
                count = heapq.heappop_max(maxHeap)
                newCount = count - 1
                if newCount > 0:
                    queue.append([newCount, cycles + n])
            
            if queue and queue[0][1] == cycles:
                val = queue.popleft()[0]
                heapq.heappush_max(maxHeap, val)
        return cycles

