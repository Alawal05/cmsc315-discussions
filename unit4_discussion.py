"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # Each node has a value and space for left and right children.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # An empty tree has no root node yet.
        self.root = None

    def insert(self, value):
        # Begin at the root and use the helper to find the right spot.
        # Smaller values go left, and larger values go right.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        # An empty position means we can create a new node here.
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        # We ignore duplicates instead of adding the same number twice.
        return node

    def search(self, value):
        # Start at the root and search only the side that could
        # contain the value, instead of checking every node.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None:
            return False  # We reached an empty spot; no match.
        if value == node.value:
            return True
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def inorder(self):
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        if node is not None:
            # Left, current node, then right gives sorted values
            # because every left value is smaller than its parent.
            self._inorder_recursive(node.left, values)
            values.append(node.value)
            self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # BUILD A TREE
    print("\n=== TREE CONSTRUCTION ===")
    tree = BST()
    numbers = [50, 30, 70, 20, 40, 60, 80]
    for number in numbers:
        tree.insert(number)
    print("Values inserted:", numbers)
    # For a balanced tree like this one, comparisons let us
    # rule out about half the remaining values at each step.

    # IN-ORDER TRAVERSAL
    print("\n=== IN-ORDER TRAVERSAL ===")
    print("In-order traversal:", tree.inorder())
    # The left-root-right order puts these values in ascending order.

    # SEARCH TESTS
    print("\n=== SEARCH TESTS ===")
    # These two values were inserted, so both searches return True.
    print("Searching for 30:", tree.search(30))
    print("Searching for 70:", tree.search(70))
    # Neither value was inserted, so both searches return False.
    print("Searching for 25:", tree.search(25))
    print("Searching for 90:", tree.search(90))

    # EDGE CASES
    print("\n=== EDGE CASES ===")
    empty_tree = BST()
    # With no root node, there is nothing to find or traverse.
    print("Searching an empty tree for 10:", empty_tree.search(10))
    print("In-order traversal of empty tree:", empty_tree.inorder())
    # Duplicates are ignored, so inserting 30 again changes nothing.
    tree.insert(30)
    print("After inserting duplicate 30:", tree.inorder())


if __name__ == "__main__":
    main()
