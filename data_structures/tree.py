"""
Custom Tree Implementation
Binary tree and general tree structures.
"""

from typing import Optional, List, Any


class TreeNode:
    """Represents a node in a general tree."""
    
    def __init__(self, value: Any):
        self.value = value
        self.children: List['TreeNode'] = []
        self.parent: Optional['TreeNode'] = None
    
    def add_child(self, child: 'TreeNode'):
        """Add a child node."""
        child.parent = self
        self.children.append(child)
    
    def get_children(self) -> List['TreeNode']:
        """Return list of children."""
        return self.children
    
    def is_leaf(self) -> bool:
        """Check if node is a leaf."""
        return len(self.children) == 0
    
    def __repr__(self):
        return f"TreeNode({self.value})"


class BinaryTree:
    """
    Custom Binary Tree implementation.
    Each node can have at most two children (left and right).
    """
    
    class Node:
        """Binary tree node."""
        def __init__(self, value: Any):
            self.value = value
            self.left: Optional['BinaryTree.Node'] = None
            self.right: Optional['BinaryTree.Node'] = None
            self.parent: Optional['BinaryTree.Node'] = None
        
        def __repr__(self):
            return f"Node({self.value})"
    
    def __init__(self):
        self.root: Optional[BinaryTree.Node] = None
        self._size = 0
    
    def insert(self, value: Any) -> 'BinaryTree.Node':
        """Insert a value into the binary tree (level-order insertion)."""
        new_node = BinaryTree.Node(value)
        
        if self.root is None:
            self.root = new_node
            self._size += 1
            return new_node
        
        # Level-order insertion using a queue
        from .queue import Queue
        queue = Queue()
        queue.enqueue(self.root)
        
        while not queue.is_empty():
            current = queue.dequeue()
            
            if current.left is None:
                current.left = new_node
                new_node.parent = current
                self._size += 1
                return new_node
            else:
                queue.enqueue(current.left)
            
            if current.right is None:
                current.right = new_node
                new_node.parent = current
                self._size += 1
                return new_node
            else:
                queue.enqueue(current.right)
        
        return new_node
    
    def inorder_traversal(self, node: Optional['BinaryTree.Node'] = None) -> List[Any]:
        """Perform inorder traversal (left, root, right)."""
        if node is None:
            return self._inorder_helper(self.root)
        return self._inorder_helper(node)
    
    def _inorder_helper(self, node: Optional['BinaryTree.Node']) -> List[Any]:
        """Helper for inorder traversal."""
        if node is None:
            return []
        
        result = []
        result.extend(self._inorder_helper(node.left))
        result.append(node.value)
        result.extend(self._inorder_helper(node.right))
        return result
    
    def preorder_traversal(self, node: Optional['BinaryTree.Node'] = None) -> List[Any]:
        """Perform preorder traversal (root, left, right)."""
        if node is None:
            return self._preorder_helper(self.root)
        return self._preorder_helper(node)
    
    def _preorder_helper(self, node: Optional['BinaryTree.Node']) -> List[Any]:
        """Helper for preorder traversal."""
        if node is None:
            return []
        
        result = [node.value]
        result.extend(self._preorder_helper(node.left))
        result.extend(self._preorder_helper(node.right))
        return result
    
    def postorder_traversal(self, node: Optional['BinaryTree.Node'] = None) -> List[Any]:
        """Perform postorder traversal (left, right, root)."""
        if node is None:
            return self._postorder_helper(self.root)
        return self._postorder_helper(node)
    
    def _postorder_helper(self, node: Optional['BinaryTree.Node']) -> List[Any]:
        """Helper for postorder traversal."""
        if node is None:
            return []
        
        result = []
        result.extend(self._postorder_helper(node.left))
        result.extend(self._postorder_helper(node.right))
        result.append(node.value)
        return result
    
    def size(self) -> int:
        """Return the number of nodes in the tree."""
        return self._size
    
    def __len__(self):
        return self._size
    
    def __repr__(self):
        return f"BinaryTree(size={self._size})"
