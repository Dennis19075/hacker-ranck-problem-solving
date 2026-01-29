#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY 'a' as parameter.
#
# 29/01/2026

from collections import Counter

def pickingNumbers(a):
    occurrences = Counter(a)
    max_count = 0
    for number in occurrences:
        current_count = occurrences[number] + occurrences[number + 1]
        if current_count > max_count:
            max_count = current_count
    return max_count

a = [1,1,2,2,4,4,5,5,5]

print(pickingNumbers(a))

# I have learned: 
# - Counter gives an unordered dict
# - number is a key unique value
# - if we use the occurrences[number] and occurrences[number+1] 
# this guarantees the abs diff is 1 or less
# - update the max count with the newest max value
