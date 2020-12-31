from test_framework import generic_test

def count_bits(x: int) -> int:
    c = 0
    while x:
        x &= x - 1
        c += 1

    return c

def parity(x: int) -> int:
    return count_bits(x) % 2

def parity2(x: int) -> int:
    x ^= x >> 64
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1

    return x & 1

if __name__ == '__main__':
    generic_test.generic_test_main('parity.py', 'parity.tsv', parity)
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity2))
