# 1. Create a function that iterates each field for each filed.
# 2. Find the minimmum distance to any tower
# 3. Find the maximum of these minimum distances
# 4. import math for getting the absolute value

import math
def maxPower(fields, towers):
    maximumPower = 0
    for field in fields:
        minDistance = float('inf')
        for tower in towers:
            distance = math.fabs(field - tower)
            if distance < minDistance:
                minDistance = distance
        if minDistance > maximumPower:
            maximumPower = minDistance
    return maximumPower

# NB. This is a brute force solution with a time complexity of O(n2). 
