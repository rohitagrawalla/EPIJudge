from itertools import product
from typing import List

from test_framework import generic_test, test_utils

MAPPING = ("0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ")


def phone_mnemonic(phone_number: str) -> List[str]:
    numbers = list(map(int, phone_number))
    string_choices = [MAPPING[n] for n in numbers]

    mnemonics = product(*string_choices)

    return ["".join(x) for x in mnemonics]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            "phone_number_mnemonic.tsv",
            phone_mnemonic,
            comparator=test_utils.unordered_compare,
        )
    )