# *
# * *
# * * *
# * * * *
# * * * * *

""" Here if we observe this pattern as in first row we have 1 star
    in 2nd row we have 2 star similarly in 5 row 5 star from there
    we get this logic inner loop j runs less than the row """
n = 5
for i in range(1, n+1):  # Here is outer loop is to print rows
    for j in range(0, i):  # Here this inner loop to print column
        print('*', end=' ')
    print()
