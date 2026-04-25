class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
        def to_day(date):
            month = int(date[:2])
            day = int(date[3:])
            
            return sum(days_in_month[:month-1]) + day
        
        a_start = to_day(arriveAlice)
        a_end = to_day(leaveAlice)
        b_start = to_day(arriveBob)
        b_end = to_day(leaveBob)

        overlap_start = max(a_start, b_start)
        overlap_end = min(a_end, b_end)
        
        if overlap_start > overlap_end:
            return 0
        
        return overlap_end - overlap_start + 1
        