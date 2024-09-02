# *
# * *
# * * *
# * * * *
# * * * * *

""" Here if we observe this pattern as in first row we have 1 star
    in 2nd row we have 2 star similarly in 5 row 5 star from there
    we get this logic inner loop j runs less than the row """
n = 5
for i in range(1, n + 1):  # Here is outer loop is to print rows
    for j in range(0, i):  # Here this inner loop to print column
        # print('*', end=' ')
        pass
    # print()
    pass
#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *

n = 5
# for i in range(0, n):
#     j = k = l = 0
#     while j < n - i - 1:
#         print(' ', end='')
#         j += 1
#     while k < 2 * i + 1:
#         print('*', end='')
#         k += 1
#     while l < n - i - 1:
#         print(' ', end='')
#         l += 1
#     print()
#
# for i in range(0, n):
#     j = k = m = 0
#     while j < i:
#         print(' ', end='')
#         j += 1
#     while k < 2 * n - (2 * i + 1):
#         print('*', end='')
#         k += 1
#     while m < i:
#         print(' ', end='')
#         m += 1
#     print()


# for i in range(1, n + 1):
#
#     start = 1
#
#     start = 1 if i % 2 else 0
#
#     for j in range(0, i):
#         print(start, end=' ')
#         start = 1 - start
#     print()

# for i in range(1, n+1):
#     for j in range(i):
#         print((i + j) % 2, end=" ")
#     print()


n = 5

for i in range(n, -1, -1):
    for j in range(i, 0, -1):
        print('*', end='')
    print()
