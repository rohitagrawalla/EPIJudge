import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def search_entry_equal_to_its_index(A: List[int]) -> int:
    b, e = 0, len(A)

    while b < e:
        m = b + (e - b) // 2
        if A[m] > m:
            e = m
        elif A[m] < m:
            b = m + 1
        else:
            return m

    return -1


@enable_executor_hook
def search_entry_equal_to_its_index_wrapper(executor, A):
    result = executor.run(functools.partial(search_entry_equal_to_its_index,
                                            A))
    if result != -1:
        if A[result] != result:
            raise TestFailure('Entry does not equal to its index')
    else:
        if any(i == a for i, a in enumerate(A)):
            raise TestFailure('There are entries which equal to its index')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'search_entry_equal_to_index.py',
            'search_entry_equal_to_index.tsv',
            search_entry_equal_to_its_index_wrapper))
