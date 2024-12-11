from typing import Any

class Node:
    def __init__(self, key: int) -> None:
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def __lt__(self, other):
        if other is None:
            return False
        return self.key < other.key
    
    def __gt__(self, other):
        if other is None:
            return False
        return self.key > other.key
    
    def __eq__(self, other):
        if other is None:
            return False
        return self.key == other.key
    
    def __ge__(self, other):
        if other is None:
            return False
        return self.key >= other.key
    
    def __le__(self, other):
        if other is None:
            return False
        return self.key <= other.key

class BST:
    def __init__(self) -> None:
        self.root = None

    def isEmpty(self) -> bool:
        if self.root is None:
            return True
        else:
            return False
        
    def insert(self, key: int) -> Node:
        node_new = Node(key)
        if self.root is None:
            self.root = node_new
            return self.root

        node_current = self.root
        while True:
            if key < node_current.key:
                if node_current.left is None:
                    node_current.left = node_new
                    node_new.parent = node_current
                    return node_new
                else:
                    node_current = node_current.left
            elif key > node_current.key:
                if node_current.right is None:
                    node_current.right = node_new
                    node_new.parent = node_current
                    return node_new
                else:
                    node_current = node_current.right
            else:
                # Duplicate keys are not allowed, do nothing or handle as needed
                return node_current
    def search(self, key: int) -> Node:
        node_current = self.root
        if node_current is None:
            return None

        while True:
            if key == node_current.key:
                return node_current
            elif key < node_current.key:
                if node_current.left is None:
                    break
                node_current = node_current.left
            else:
                if node_current.right is None:
                    break
                node_current = node_current.right

        return
    
    def max(self, node: Node = None) -> Node:
        if node is None:
            node = self.root

        node_current = node
        while True:
            if node_current.right is None:
                break
            node_current = node_current.right

        return node_current

    def min(self, node: Node = None) -> Node:
        if node is None:
            node = self.root

        node_current = node
        while True:
            if node_current.left is None:
                break
            node_current = node_current.left

        return node_current

    def inOrderPredecessor(self, key: int) -> Node:
        node_current = self.root
        predecessor = None

        while node_current is not None:
            if key == node_current.key:
                # Node with the given key found
                if node_current.left is not None:
                    # Find the max in the left subtree
                    predecessor = self.max(node_current.left)
                return predecessor
            elif key < node_current.key:
                node_current = node_current.left
            else:
                # Update predecessor to the current node when going right
                predecessor = node_current
                node_current = node_current.right

        return


    def inOrderSuccessor(self, key: int) -> Node:
        node_current = self.root
        successor = None

        while node_current is not None:
            if key == node_current.key:
                # Node with the given key found
                if node_current.right is not None:
                    # Find the min in the right subtree
                    successor = self.min(node_current.right)
                return successor
            elif key < node_current.key:
                # Update successor to the current node when going left
                successor = node_current
                node_current = node_current.left
            else:
                node_current = node_current.right

    def preOrderPredecessor(self, key: int) -> Node:
        node_current = self.root
        predecessor = None
        node_stack = []

        while node_current is not None or node_stack:
            while node_current is not None:
                if node_current.key == key:
                    return predecessor
                node_stack.append(node_current)
                predecessor = node_current
                node_current = node_current.left
            node_current = node_stack.pop()
            node_current = node_current.right

        return

    def preOrderSuccessor(self, key: int) -> Node:
        node_current = self.root
        node_stack = []
        node_before = None

        while node_stack or node_current:
            while node_current is not None:
                if node_before and node_before.key == key:
                    return node_current
                node_stack.append(node_current)
                node_before = node_current
                node_current = node_current.left

            node_current = node_stack.pop()
            node_current = node_current.right

        return

    def postOrderPredecessor(self, key: int) -> Node:
        if not self.root:
            return

        node_stack = []
        node_checked = None
        node_current = self.root
        prev = None

        while node_stack or node_current:
            if node_current:
                node_stack.append(node_current)
                node_current = node_current.left
            else:
                top_node = node_stack[len(node_stack)-1]
                if top_node.right and node_checked != top_node.right:
                    node_current = top_node.right
                else:
                    node_checked = node_stack.pop()
                    if node_checked.key == key:
                        return prev
                    prev = node_checked

        return

    def postOrderSuccessor(self, key: int) -> Node:
        if not self.root:
            return

        node_stack = []
        node_checked = None
        node_current = self.root
        prev = None

        while node_stack or node_current:
            if node_current:
                node_stack.append(node_current)
                node_current = node_current.left
            else:
                top_node = node_stack[len(node_stack)-1]
                if top_node.right and node_checked != top_node.right:
                    node_current = top_node.right
                else:
                    node_checked = node_stack.pop()
                    if prev and prev.key == key:
                        return node_checked
                    prev = node_checked

        return
