class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        total_length = len(timeSeries) * duration
        for i in range(len(timeSeries)-1):
            dist = timeSeries[i+1]-timeSeries[i]
            if dist < duration:
                total_length -= duration - dist
        return total_length


test_list = [1,3]
test = 2

print Solution().findPoisonedDuration(test_list, test)