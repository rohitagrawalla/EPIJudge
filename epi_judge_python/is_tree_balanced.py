from typing import NamedTuple

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    class BalancedResult(NamedTuple):
        is_balanced: bool
        height: int

    def check_balanced_tree(tree: BinaryTreeNode) -> BalancedResult:
        if not tree:
            return BalancedResult(True, -1)

        left_result = check_balanced_tree(tree.left)
        if not left_result.is_balanced:
            return BalancedResult(False, 0)
        
        right_result = check_balanced_tree(tree.right)
        if not right_result.is_balanced:
            return BalancedResult(False, 0)

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedResult(is_balanced, height)


    return check_balanced_tree(tree).is_balanced


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_tree_balanced.py", "is_tree_balanced.tsv", is_balanced_binary_tree
        )
    )
