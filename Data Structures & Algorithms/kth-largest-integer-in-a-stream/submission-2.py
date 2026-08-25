class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.numbers = nums

    def add(self, val: int) -> int:
        
        self.numbers.append(val)
        self.numbers.sort()
        n = len(self.numbers)
        return self.numbers[n - self.k]
        
