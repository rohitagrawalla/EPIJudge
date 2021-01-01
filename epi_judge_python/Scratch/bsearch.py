from typing import List, Optional


def bsearch(A: List[int], s: int) -> Optional[int]:
    # Range is always represented as open closed range [begin, end)
    l, u = 0, len(A)
    m = 0
    while l < u:
        m = l + (u - l) // 2

        # Now we consider the range [l, m), m, [m+1, u)
        if s < A[m]:
            u = m
        elif s > A[m]:
            l = m + 1
        else:
            return m

    print(f"{l=}|{m=}|{u=}")
    return None


if __name__ == "__main__":
    print(bsearch(list(range(0, 100, 2)), 73))
    print(bsearch([], 0))
