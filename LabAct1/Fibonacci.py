def recursive(n):
  if n < 0:
    result = "Invalid input. Please enter a non-negative integer."
  elif n <= 1:
    result = n
  else:
    result = recursive(n - 1) + recursive(n - 2)
  return result
  
def iterative(n):
  if n < 0:
    result = "Invalid input. Please enter a non-negative integer."
  elif n <= 1:
    result = n
  else:
    a, b = 1, 1
    for i in range(n - 2):
      a, b = b, a + b
      result = b
    return result

n=6
if n < 0:
  print("\n" + recursive(n) +"\n")
else:
  print(f"\nThe Fibonacci number {n} using recursion is {recursive(n)}.\n")
  print(f"The Fibonacci number {n} using iteration is {iterative(n)}.\n")