from typing import List, TypeVar


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


if __name__ == "__main__":
    print(lower_bound([0], 1))
