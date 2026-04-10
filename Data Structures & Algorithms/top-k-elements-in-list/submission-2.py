class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Dictionary to count the frequency of each number in the input list
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # 2. Convert the dictionary into a list of [frequency, number] pairs
        # This helps in sorting the numbers based on frequency
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])

        # 3. Sort the list in ascending order by frequency
        arr.sort()

        # 4. Pop the last k elements from the sorted list (which are the most frequent)
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])  # Get the number (not the count)
        return res
