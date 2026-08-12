class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # important to note: if nums has length n,
        # then it has indices [0, n-1]
        # and the values at those indices can be in [1, n-1]
        # therefore, the values can be used as indices into nums
        # (a linked list!) because the values are always a valid index in nums.

        # example: list [1, 3, 4, 2, 2] as a linked list becomes
        # 1 -> 3 -> 2 -> 4 -> 2 -> 4 -> ...
        # a couple properties of this linked list:
        # - since no value is 0, the linked list can always start at index 0
        # - there will always be a cycle

        # Floyd's cycle detection algorithm:
        # In a graph with a cycle whose cycle starts at node C,
        # if a slow pointer and fast pointer moving twice as fast start at node A
        # and intersect at node B,
        # the distance from A to C is equal to the distance from B to C.

        # slowPtr1 == fastPtr == A
        slowPtr1 = 0
        fastPtr = 0

        while slowPtr1 == 0 or slowPtr1 != fastPtr:
            slowPtr1 = nums[slowPtr1]
            fastPtr = nums[nums[fastPtr]]
        
        # slowPtr1 == fastPtr == B

        slowPtr2 = 0
        # slowPtr2 == A

        while slowPtr1 != slowPtr2:
            slowPtr1 = nums[slowPtr1]
            slowPtr2 = nums[slowPtr2]
        
        # slowPtr1 == slowPtr2 == C
        return slowPtr1

            