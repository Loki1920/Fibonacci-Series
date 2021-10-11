# display Fibonacci series
d = {}
def Fibonacci(n):
  if(n in d):
    return d[n]
  if (n <= 1):
    return(n)
  else:
    variableValue = (Fibonacci(n-1) + Fibonacci(n-2))
    d[n]=variableValue
    return(variableValue)
# user input
n = int(input("enter a number:"))
if n <= 0:
  print("enter a positive number:")
else:
  print("Fibonacci series is :")
  print(Fibonacci(n))





  