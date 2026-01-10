class Solution:
    def dayOfYear(self, date: str) -> int:

        days_in_month = [0, 31, 28 , 31, 30, 31, 30, 31, 31, 30, 31, 30 , 31]

        month = int(date.split('-')[1])

        days = sum(days_in_month[:month]) + int(date.split('-')[2]) +  (1 if (self.isLeapYear(int(date.split('-')[0]))) and month>2 else 0)

        return days

    
    def isLeapYear(self, year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        