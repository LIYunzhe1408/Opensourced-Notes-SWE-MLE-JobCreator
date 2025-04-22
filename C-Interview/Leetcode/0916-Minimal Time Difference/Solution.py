'''
Cannot pass test cases
'''
class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        for i, time in enumerate(timePoints):
            timePoints[i] = time.split(":")
        
        sortedTimes = sorted(timePoints, key=lambda x: int(x[0]))
        

        print(sortedTimes)
        minimum = 1440
        for i in range(0, len(sortedTimes)-1):
            diffOffset = 1440
            if int(sortedTimes[i][0]) == 0:
                diffOffset = abs(int(24*60 + int(sortedTimes[i][1]) - int(sortedTimes[i+1][0])*60 - int(sortedTimes[i+1][1])))
            diff = abs(int(sortedTimes[i+1][0])*60 + int(sortedTimes[i+1][1]) - int(sortedTimes[i][0])*60 - int(sortedTimes[i][1]))
            if diffOffset < diff:
                diff = diffOffset
            if diff < minimum:
                minimum = diff
            print(diff, diffOffset, minimum)
        
        diff = abs(24*60 + int(sortedTimes[0][0])*60 + int(sortedTimes[0][1]) - int(sortedTimes[-1][0])*60 - int(sortedTimes[-1][1]))
        if diff < minimum:
            minimum = diff


        return minimum
    

'''
Revised: Convert to minutes first.
'''
class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        for i, time in enumerate(timePoints):
            hourMin = time.split(":")
            timePoints[i] = int(hourMin[0])*60 + int(hourMin[1])
        
        sortedTimes = sorted(timePoints)

        minimum = 1440
        for i in range(0, len(sortedTimes)-1):
            minimum = min(minimum, sortedTimes[i+1]- sortedTimes[i])
        

        return min(minimum, 1440 + sortedTimes[0] - sortedTimes[-1])

'''
Avoid Sorting
'''
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert(time):
            hh, mm = time.split(':')
            return int(hh) * 60 + int(mm)

        time_slots = [False] * 1440
        start, end = 1440, -1
        for time in timePoints:
            minutes = convert(time)
            if time_slots[minutes]:
                return 0

            time_slots[minutes] = True
            start = min(start, minutes)
            end = max(end, minutes)

        prev, res = start, start - end + 1440
        for curr in range(start + 1, end + 1):
            if not time_slots[curr]:
                continue

            res = min(res, curr - prev)
            prev = curr

        return res