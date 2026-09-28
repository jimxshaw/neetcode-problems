class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myDict = {}

        # Empty list.
        if not nums:
            return False

        # List with only 1 element.
        if len(nums) < 2:
            return False

        for num in nums:
            if num in myDict:
                return True
            else:
                myDict[num] = num

        return False

        