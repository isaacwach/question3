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

#OPTIMAL SOLUTION USING BINARY SEARCH

# 1. create a function that takes fields and towers as arguments
# 2. Create a default dictionary
# 3. Initialise maximun distance and assign it an infinity float
# 4. Initialise a current minimums (curr_mins) variable and assign it the absolute value of the diference between field and towers at each index
# 5. Loop through the curr_mins and map keys to values
# 6. Get the largest value of the curr_mins and return it as the maximum distance
# 7. Create another function that takes an array an target as the arguments.
# 8. Initalize left and right pointers at 0 index an end of array, respectively
# 9. Use conditional statements to compare the values at left and right pointers
# 10. if right equals left, return 0
# 11. Whenever right is greater than left, get the mid  

def solution2(field, towers):

    curr_mins = defaultdict(list)
    max_distance = float('-inf')
    for field in fields: 
        tower_index = binarysearch(towers, field)
        distance = abs(field - towers[tower_index]) 
        curr_mins[field].append(distance)
    for k, v in curr_mins.items():
        max_distance  = max(max_distance, v[0])

    return max_distance

def binarysearch(array, target):
    left, right = 0, len(array) - 1
    if right == left:
        return 0
    if right == 1:
        if abs(array[0] - target) < abs(array[1] - target):
            return 0
        else: return 1
    
    while left < right :
        mid = (left + right) // 2
        if target == array[mid] or abs(array[mid] - target)  == abs(array[mid+1] - target) :
            return mid 
        elif abs(array[mid] - target)  < abs(array[mid+1] - target):
            right = mid -1 
        else:
            left = mid 
        if mid == len(array) -1:
            break
    return mid 



fields = [1, 2, 3, 4]
towers = [1, 4]
print(solution2(fields, towers))