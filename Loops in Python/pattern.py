# for row in range (1, 5):
#     for column in range(row):
#         print("*", end="")
#     print()




# for row in range(4, 0, -1):
#     for column in range(row):
#         print("*", end="")
#     print()




# n = 4
# for row in range(1, n + 1):
#     for spaces in range(n-row):
#         print(" ", end="")
#     for stars in range(row):
#         print("*", end="")
#     print()



# n = 4
# for row in range(1, n + 1):
#     for spaces in range(n - row):
#         print(" ", end="")
#     for stars in range(2 * row - 1):
#         print("*", end="")
#     print()





# for row in range(1, 5):
#     for column in range(1, row + 1):
#         print(column, end="") 
#     print()






# for row in range(4):
#     for column in range(4):
#         print("*", end="")
#     print()




# n = 4
# for row in range(1, n + 1):
#     for column in range(-1, n - row):
#         print("*", end="")
#     print()





# for row in range(1, 5):
#     for column in range(row):
#         print(row, end="")
#     print()





'''

****
*  *
*  *
****

'''

# n = 4
# for row in range(1, n+1):
#     for column in range(1, n+1):
#         if row == 1 or row == n or column == 1 or column == n:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()






'''

   1
  121
 12321
1234321

'''

n = 4
for row in range(1, n + 1):

    # Spaces
    for column in range(n - row):
        print(" ", end="")
    
    # Increasing Numbers
    for num in range(1, row + 1):
        print(num, end="")
    
    
    # Decreasing Numbers
    for renum in range(row - 1):
        print(row - renum - 1, end="")
    print()

