from typing import List, Set

from test_framework import generic_test

def has_two_sum(A: Set[int], t: int) -> bool:
    return any(t - a in A for a in A)

def has_three_sum(A: List[int], t: int) -> bool:
    set_A = set(A)
    return any(has_two_sum(set_A, t - it) for it in A)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                       has_three_sum))
