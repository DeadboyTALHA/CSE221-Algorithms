class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createTree(inorder, preorder):
    if not inorder:
        return None
    root_val = preorder[0]
    root = TreeNode(root_val)
    mid = 0
    while mid < len(inorder) and inorder[mid] != root_val:
        mid += 1
    root.left = createTree(inorder[:mid], preorder[1:mid+1])
    root.right = createTree(inorder[mid+1:], preorder[mid+1:])
    return root

def postorderTraversal(root):
    if root == None:
        return []
    return postorderTraversal(root.left) + postorderTraversal(root.right) + [root.val]

N = int(input())
inorder = list(map(int, input().split()))
preorder = list(map(int, input().split()))
root = createTree(inorder, preorder)
ans = postorderTraversal(root)
print(' '.join(map(str, ans)))