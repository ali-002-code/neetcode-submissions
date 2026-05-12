# defaultdict automatically creates missing keys
# int means missing keys start with value 0
from collections import defaultdict 


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # hashmap stores:
        # number -> frequency
        counts = defaultdict(int)

        # count frequency of each number
        for num in nums:
            counts[num] += 1

        # counts.items() converts dictionary into:
        # [(key, value), (key, value)]
        # example:
        # [(1,1), (2,2), (3,3)]

        # sorted() sorts the list
        # key=lambda x: x[1] means:
        # sort using the SECOND value in each tuple
        # x[0] = number
        # x[1] = frequency

        # reverse=True means highest frequencies first
        sorted_items = sorted(
            counts.items(),
            key=lambda x: x[1],
            reverse=True
        )

        result = []

        # sorted_items[:k] takes first k elements
        # each element is:
        # (num, frequency)

        for num, freq in sorted_items[:k]:
            result.append(num)

        return result