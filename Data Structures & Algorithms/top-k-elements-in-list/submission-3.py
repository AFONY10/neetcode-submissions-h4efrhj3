import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Use Counter to get frequency of each number
        count = Counter(nums)

        # 2. Build a max-heap by pushing (-frequency, number) pairs
        # Negative frequency is used because heapq is a min-heap
        max_heap = []
        for num, freq in count.items():
            heapq.heappush(max_heap, (-freq, num))

        # 3. Extract the top k elements from the heap
        result = []
        for _ in range(k):
            result.append(heapq.heappop(max_heap)[1])  # Get the number (not the frequency)

        return result
