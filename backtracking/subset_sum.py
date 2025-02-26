"""
The subset sum problem
"""

def subset_sum(set: list[int], sum: int) -> bool:
    if sum == 0:
        return True
    elif sum < 0 or len(set) == 0:
        return False

    x = set[-1]
    without_x = set[:-1]

    return subset_sum(without_x, sum - x) or subset_sum(without_x, sum)

test_set = [2, 3, 4, 3]
test_sum = 6
print(subset_sum(test_set, test_sum))


