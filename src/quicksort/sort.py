from partition import partition

def sort(data, left, right):
  if right <= left:
    return
  else:
    pivot = partition(data, left, right)
    sort(data, left, pivot - 1)
    sort(data, pivot + 1, right)

  return data
