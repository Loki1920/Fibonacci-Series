# display Fibonacci series
def Fibonacci(n):
  if (n <= 1):
    return(n)
  else:
    return(Fibonacci(n-1) + Fibonacci(n-2))
# user input
n = int(input("enter a number :"))

if n <= 0:
  print("enter a positive number:")
else:
  print("Fibonacci series is :")
  for i in range(n):
    print(Fibonacci(i))

  





  