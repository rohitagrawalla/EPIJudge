from typing import List

from test_framework import generic_test


def lower_bound(A: List[int], t: int) -> int:
    b, e = 0, len(A)

    while b < e:
        m = b + (e - b) // 2

        if A[m] < t:
            # A[b..m+1) does not contain valid candidate for lower bound (not less than t)
            b = m + 1
        else:
            # A[m] >= t, a candidate for 
            # A[b..m) contains a valid candidate for low bound
            e = m

    return b

def search_first_of_k(A: List[int], k: int) -> int:
    lb = lower_bound(A, k)    
    return lb if lb < len(A) and A[lb] == k else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
