# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        _attributes = [attr for attr in dir(p) if not callable(getattr(p, attr)) and not attr.startswith("__")]
        print(_attributes)
        return True

if __name__ == '__main__':
    p = [1,2,3]
    q = [1,2,3]

    """ p = [1,2]
    q = [1,null,2] """

    """ p = [1,2,1]
    q = [1,1,2] """
    
    p_tree_node = TreeNode(p[0],p[1],p[2])
    q_tree_node = TreeNode(q[0],q[1],q[2])

    solution = Solution()
    is_the_same = solution.isSameTree(p_tree_node,q_tree_node)

    if is_the_same:
        print("The trees are the same")
    else:
        print("The trees aren't the same")

    