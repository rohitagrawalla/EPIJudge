from test_framework import generic_test


def closest_int_same_bit_count(x: int) -> int:
    NUM_BITS = 64
    for i in range(NUM_BITS - 1):
        if (x >> i) & 1 != (x >> (i + 1)) & 1:
            x ^= (1 << i) | (1 << (i + 1))  # Swapsbit-i andbit-(i +1) return x
            return x

    return x

if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "closest_int_same_weight.py",
            "closest_int_same_weight.tsv",
            closest_int_same_bit_count,
        )
    )
