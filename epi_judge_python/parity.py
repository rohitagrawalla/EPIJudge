from test_framework import generic_test

def count_bits(x: int) -> int:
    c = 0
    while x:
        x &= x - 1
        c += 1

    return c

def parity(x: int) -> int:
    return count_bits(x) % 2


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
