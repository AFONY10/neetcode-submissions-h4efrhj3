class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        countDict = Counter(tasks)
        maxHeap = list(countDict.values())
        heapq.heapify_max(maxHeap)

        queue = deque()
        time = 0

        while maxHeap or queue:
            time += 1

            if maxHeap:
                currCount = heapq.heappop_max(maxHeap)
                updCount = currCount - 1

                if updCount > 0:
                    queue.append([updCount, time + n])
            if queue and queue[0][1] == time:
                countVal = queue.popleft()[0]
                heapq.heappush_max(maxHeap, countVal)
        return time

