class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
       
        for i in range(len(arr)):
            print(seen)
            if (arr[i]*2 in seen) or (arr[i] % 2 == 0 and arr[i] // 2 in seen):
                return True
            else:
                seen.add(arr[i])

        return False  


        