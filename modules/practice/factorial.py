def factorial(n):
  print("factorial called with n = ", str(n))
  if n == 1 or n == 0:
    print("Ending condition met.")
    return 1
  else:
    return n * factorial(n - 1)

print(factorial(10))