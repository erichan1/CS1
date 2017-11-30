
# A.1.1
def union(s1, s2):
    unionSet = set()
    for element in s1:
        unionSet.add(element)
    for element in s2:
        unionSet.add(element)
    return unionSet

# A.1.2
def intersection(s1, s2):
    intersectSet = set()
    for element in s1:
        if element not in s2:
            intersectSet.add(element)
    for element in s2:
        if element not in s1:
            intersectSet.add(element)
    return intersectSet

# A.2
def mySum(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum
