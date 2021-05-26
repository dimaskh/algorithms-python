def partition(data, left, right):
  pivot = data[left]
  leftIndex = left + 1
  rightIndex = right

  while True:
    while leftIndex <= rightIndex and data[leftIndex] <= pivot:
      leftIndex += 1
    while rightIndex >= leftIndex and data[rightIndex] >= pivot:
      rightIndex -= 1
    if rightIndex <= leftIndex:
      break
    data[leftIndex], data[rightIndex] = data[rightIndex], data[leftIndex]
    print(data)

  data[left], data[rightIndex] = data[rightIndex], data[left]
  print(data)

  return rightIndex
