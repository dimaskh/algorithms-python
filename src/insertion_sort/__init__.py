data = [9, 5, 7, 4, 2, 8, 1, 10, 6, 3]

for scanIndex in range(1, len(data)):
  temp = data[scanIndex] # 5
  minIndex = scanIndex # 1

  while minIndex > 0 and temp < data[minIndex - 1]:
    data[minIndex] = data[minIndex - 1]
    minIndex -= 1

  data[minIndex] = temp
  print(data)
