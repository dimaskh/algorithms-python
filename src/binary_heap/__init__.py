import heapq
from data import data

heap = []

for key, value in data.items():
  heapq.heappush(heap, (key, value))

heapq.heappush(heap, (6, 'Teal'))

heap.sort()

for item in heap:
  print('Key: ', item[0], 'Value: ', item[1])

print('Item 3 contains: ', heap[3][1])
print('The maximum item is: ', heapq.nlargest(1, heap))
