#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

# def choose(n, k):
#   if k == 0:
#     return 1  # there's only one option to choose zero items out of n
#   elif n < k:
#     return 0  # there's no way to choose k of n when k > n
#   else:
#     # The recursion: you can do either
#     # 1. choose the n-th element and then the rest k-1 out of n-1
#     # 2. or choose all the k elements out of n-1 (not choose the n-th element)
#     return choose(n - 1, k - 1) + choose(n - 1, k)

def eating_cookies(n, k):
  if k == 0:
    return 1
  else:
    return eating_cookies(n - 1, k - 1) + eating_cookies(n - 1, k)

result = eating_cookies(50, 3)

print(result)

# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_cookies = int(sys.argv[1])
#     print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
#   else:
#     print('Usage: eating_cookies.py [num_cookies]')