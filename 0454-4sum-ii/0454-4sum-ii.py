class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count_map = defaultdict(int)
        print(count_map)
    
        # Step 1: Store sums of all pairs from nums1 and nums2
        for a in nums1:
            for b in nums2:
                count_map[a + b] += 1

        print("nnw", count_map)
        result = 0

        # Step 2: For each pair in nums3 and nums4, check if -(c + d) exists
        for c in nums3:
            for d in nums4:
                complement = -(c + d)
                result += count_map.get(complement, 0)

        return result
            