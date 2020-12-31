from collections import defaultdict
from typing import DefaultDict, List

from test_framework import generic_test, test_utils


def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    result: DefaultDict[str, List[str]] = defaultdict(list)

    for word in dictionary:
        result["".join(sorted(word))].append(word)

    return [anagrams for anagrams in result.values() if len(anagrams) > 1]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "anagrams.py",
            "anagrams.tsv",
            find_anagrams,
            comparator=test_utils.unordered_compare,
        )
    )
