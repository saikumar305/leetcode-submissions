class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        num_set = set(arr)
        max_len = 0
        n = len(arr)

        for i in range(n):
            for j in range(i+1, n):
                prev = arr[j]
                curr = arr[i] + prev
                curr_len = 2

                while curr in num_set:
                    prev , curr = curr , curr+prev
                    curr_len +=1
                    max_len = max(max_len, curr_len)

        return max_len

            

        