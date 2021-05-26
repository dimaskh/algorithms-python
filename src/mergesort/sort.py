from merge import merge

def sort(list):
  # Determine whether the list is broken into individual pieces
  if len(list) < 2:
    return list

  # Find the middle of the list
  middle = len(list) // 2

  # Break the list into two pieces
  left = sort(list[:middle])
  right = sort(list[middle:])

  # Merge the two sorted pieces into a large piece
  print("Left side: ", left)
  print("Right side: ", right)
  merged = merge(left, right)
  print("Merged: ", merged)
  return merged
