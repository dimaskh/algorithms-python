def traverse(tree):
  if tree.left != None:
    traverse(tree.left)
  if tree.right != None:
    traverse(tree.right)
  print(tree.nodeData)