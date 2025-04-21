def recursive(n):
  if n < 0:
    result = "Invalid input. Please enter a non-negative integer."
  elif n <=1:
    result = 1
  else:
    result = n * recursive(n - 1)
  return result

def iterative(n):
  if n < 0:
    result = "Invalid input. Please enter a non-negative integer."
  elif n <=1:
    result = 1
  else:
    result = 1
    for i in range(1, n + 1):
      result *= i
  return result

n=5
if n < 0:
  print("\n" + recursive(n) +"\n")
else:
  print(f"\nThe factorial of {n} using recursion is {recursive(n)}.\n")
  print(f"The factorial of {n} using iteration is {iterative(n)}.\n")