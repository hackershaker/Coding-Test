class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        time.sort()
        start, end = 0, 10**14
        while start < end:
            mid = int((start + end) / 2)
            trip = 0
            for bus in time:
                busTripTime = mid // bus
                if busTripTime == 0:
                    break
                trip += busTripTime
                if trip > totalTrips:
                    break
            if trip < totalTrips:
                start = mid + 1
            else:
                end = mid

        return end
