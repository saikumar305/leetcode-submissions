class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        num_set = set(arr)
        max_len = 0
        n = len(arr)

        for i in range(n):
            for j in range(i+1, n):
                prev = arr[i]
                curr = arr[j]
                curr_len = 2

                while prev + curr in num_set:
                    prev, curr = curr, prev + curr
                    curr_len += 1

                if curr_len > 2:
                    max_len = max(max_len, curr_len)

        return max_len