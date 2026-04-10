class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        mapper = defaultdict(int)
        c = 0
        for a,b in dominoes:
            key = tuple(sorted((a,b)))
            mapper[key] +=1

        for frq in mapper.values():
            c += frq * (frq - 1) // 2

        return c

        