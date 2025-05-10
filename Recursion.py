# def sum(n):
#   if n == 0:
#     return n
#   else:
#     return n + sum(n-1)
  
# n = int(input("Enter your number"))
# print(sum(n))

# def factorial(n):
#   if n == 0:
#     return 1
#   else:
#     return n * factorial(n-1)
  
# n = int(input("Enter your number"))
# print(factorial(n))

# def fib(n):
#   if n == 0 or n == 1:
#     return n
#   else:
#     return fib(n-1) + fib(n-2)
  
# n = int(input("Enter your number"))
# print(fib(n))

def exp(b,n):
  if n == 0 or n == 1:
    return b
  else:
    return b*exp(b,n-1)
  
b = int(input("Enter your base"))
n = int(input("Enter your power"))
print(exp(b,n))
