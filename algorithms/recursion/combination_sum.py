"""
Problem Statement
----------------
Given an arrays of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.  The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.  It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


Input
-----
List of integers and target sum

Output
-------
List of possible combinations
"""


def combination_sum(candidates, target):
    all_combinations = []

    def helper(remaining_sum, index, current_combination):
        if remaining_sum == 0:
            all_combinations.append(current_combination[:])
            return
        if remaining_sum < 0:
            return
        if index == len(candidates):
            return

        current_candidate = candidates[index]
        if current_candidate <= remaining_sum:
            current_combination.append(current_candidate)
            helper(remaining_sum - current_candidate, index, current_combination)
            current_combination.pop()

        helper(remaining_sum, index + 1, current_combination)

    helper(target, 0, [])
    return all_combinations


if __name__ == '__main__':
    import doctest

    doctest.testmod()
