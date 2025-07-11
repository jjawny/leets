from typing import List


class Solution:
    def carFleet(self, target: int, positions: List[int], speeds: List[int]) -> int:
        """
        TIME: Always O(n log n):
            - Because of the sorting call to get [cars]
            - Sorted Python 3.11+ uses Powersort, costing O(n log n)
        MEMORY: Always O(n) to store:
            - cars: list of n tuples
            - fleetTTA: stack worst-case n items when no fleets merge

        ##stacks
        """

        # Mental model:
        #  We can calc the time-to-arrive (TTA) for each car
        #  If we loop over the cars in reverse order, we can use a monotonic stack (self healing stack)
        #   where we check the fleet in front, if we are faster, pop the fleet (because merging w us)
        #   but keep it's speed as slower than us, continue catching up/merging while we are faster
        #   finally append our slowest speed (the final speed) as one new fleet

        # We must sort the cars AOT to ensure our monotonic stack template works
        # Reverse order so given the curr car, we can check the stack for the fleets
        #   in front (see if curr car can catch up/merge)
        cars = sorted(zip(positions, speeds), reverse=True)

        fleetTTA = []

        # Using the monotonic stack template
        for pos, speed in cars:
            nextTTA = getTTA(pos, speed, target)
            # Can the curr car catch up to the fleet in front? merge (pop!)
            #   continue until the next fleet cannot catch up to the one in front
            while fleetTTA and nextTTA <= fleetTTA[-1]:
                nextTTA = fleetTTA.pop()
            # Save the fleet's slowest speed
            fleetTTA.append(nextTTA)

        return len(fleetTTA) # Now has the num of fleets

# TTA = time-to-arrive (lower the better)
def getTTA(pos, speed, target):
    remainingDistance = target - pos
    TTA = remainingDistance / speed
    print(f"time-to-arrive: {TTA} minutes")
    return TTA