class binaryTree:
  def __init__(self, nodeData, left = None, right = None):
    self.nodeData = nodeData
    self.left = left
    self.right = right

  def __str__(self):
    return str(self.nodeData)

def traverse(tree):
  if tree.left != None:
    traverse(tree.left)
  if tree.right != None:
    traverse(tree.right)
  print(tree.nodeData)

tree = binaryTree("Root")

BranchA = binaryTree("Branch A")
BranchB = binaryTree("Branch B")
tree.left = BranchA
tree.right = BranchB

LeafC = binaryTree("Leaf C")
LeafD = binaryTree("Leaf D")
LeafE = binaryTree("Leaf E")
LeafF = binaryTree("Leaf F")

BranchA.left = LeafC
BranchA.right = LeafD
BranchB.left = LeafE
BranchB.right = LeafF

traverse(tree)