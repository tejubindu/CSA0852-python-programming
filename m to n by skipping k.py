M = int(input("Enter the starting number of range-m: "))

N = int(input("Enter the ending number of range-n: "))

K = int(input("Enter the numbers to be skipped in range-k: "))

for i in range(M, N + 1, K+1):

   print(i)
