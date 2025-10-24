from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def breadth_first_traversal(self):
        if not self.root:
            raise Exception("Tree is empty")
        queue = deque()
        queue.append(self.root)
        visited = []
        while queue:
            visited_node = queue.popleft()
            visited.append(visited_node.data)
            if visited_node.left:
                queue.append(self.root.left)
            if visited_node.right:
                queue.append(self.root.right)
        return visited

    def dft_pre_order_iterative(self):
        if not self.root:
            raise Exception("Tree is empty")
        stack = [self.root]
        visited = []
        while stack:
            visited_node = stack.pop()
            visited.append(visited_node.data)
            if visited_node.left:
                stack.append(self.root.left)
            if visited_node.right:
                stack.append(self.root.right)
        return visited

    def dft_pre_order_recursive(self):
        if not self.root:
            raise Exception("Tree is empty")
        visited = []
        def _traverse(node):
            if not node:
                return
            visited.append(node.data)
            _traverse(node.left)
            _traverse(node.right)
        _traverse(self.root)
        return visited

    def dft_in_order_iterative(self):
        if not self.root:
            raise Exception("Tree is empty")
        current_node = self.root
        stack = []
        visited = []
        while stack or current_node:
            if current_node:
                stack.append(current_node)
                current_node = current_node.left
            else:
                visited_node = stack.pop()
                visited.append(visited_node)
                if not visited_node.right:
                    continue
                current_node = visited_node.right
        return visited

    def dft_in_order_recursive(self):
        if not self.root:
            raise Exception("Tree is empty")
        visited = []

        def _traverse(node):
            if not node:
                return
            _traverse(node.left)
            visited.append(node.data)
            _traverse(node.right)

        _traverse(self.root)
        return visited

    def dft_post_order_iterative(self):
        if not self.root:
            raise Exception("Tree is empty")
        current = self.root
        previous = self.root
        stack = []
        visited = []
        while current:
            while current.left:
                stack.append(current)
                current = current.left
            while not current.right or current.right == previous:
                visited.append(current.data)
                previous = current
                if not stack:
                    return visited
                current = stack.pop()
            stack.append(current)
            current = current.right

    def dft_post_order_recursive(self):
        if not self.root:
            raise Exception("Tree is empty")
        visited = []
        def _traverse(node):
            if not node:
                return
            _traverse(node.left)
            _traverse(node.right)
            visited.append(node.data)
        _traverse(self.root)
        return visited













