class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        container = set()

        for n in nums:
            if n in container:
                return True
            container.add(n)
        return False
            
        