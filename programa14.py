# Fibonacci: 1 1 2 3 5 8 13

num_termo = int(input())

n1 = 1
n2 = 1

fib = 0

# n1 = 1, n2 = 1, fib = 2

for contador in range(num_termo):

  fib = n1 + n2
  n1 = n2
  n2 = fib
  print(fib)