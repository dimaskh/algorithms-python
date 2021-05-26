from bintrees import BinaryTree
from data import data

tree = BinaryTree(data)
tree.update({ 6: 'Teal' })

def displayKeyValue(key, value):
  print('Key: ', key, 'Value: ', value)

tree.foreach(displayKeyValue)
print('Item 3 contains: ', tree.get(3))
print('The maximum item is: ', tree.max_item())
