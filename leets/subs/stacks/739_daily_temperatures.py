from typing import List

TemperaturePosition = tuple[int, int]

class Solution:
    # Using a stack (push, pop) we will add each temp during
    #   our main loop, "when do we pop?" before we add a new temp
    #   we pop all colder (lower) temps (stoping at >= current temp)
    #   "how do we calc the number of days each time we pop?" we will
    #   use the diff between indexes, "why not count the num of pops?"
    #   this is unreliable since temps fluctuate so we can the last 3 temps
    #   and still have an older temp to process, "how do you know the order
    #   to arrange the results?" we will re-use the index to insert the days to wait
    #   in the correct order

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        TIME: Always O(n) for the loop and initialising the waits list
        MEMORY: Always O(n) for the waits list and worst-case for the temperaturePositions if we never pop

        ##stacks ##hashmaps
        """
        waits = [0] * len(temperatures) # init all 0s by default O(n) ?
        temperaturePositions: List[TemperaturePosition] = []

        for currIdx, temp in enumerate(temperatures):
            while temperaturePositions and temperaturePositions[-1][0] < temp:
                _, prevIdx = temperaturePositions.pop()
                pastColderDays = currIdx - prevIdx
                waits[prevIdx] = pastColderDays
            temperaturePositions.append((temp, currIdx))
        return waits