from hashlib import md5, sha1

def hash_f(element, i, length):
  """ Function to create many hash functions """
  h1 = int(md5(element.encode('ascii')).hexdigest(), 16)
  h2 = int(sha1(element.encode('ascii')).hexdigest(), 16)

  return  (h1 + i * h2) % length

print(hash_f("CAT", 1, 10**5))
print(hash_f("CAT", 2, 10**5))
