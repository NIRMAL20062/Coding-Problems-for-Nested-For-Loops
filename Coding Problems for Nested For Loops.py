#Q1. Print a rectangle of stars (*) with 4 rows and 6 columns.
""" Hint: Use an outer loop for rows and an inner loop for columns.
                ******
                ******
                ******
                ****** 
"""
""" for row in range(4):
    for col in range(6):
        print("*" ,end=" ")
    print("") """


# Q2. Print one star in first row, two stars in second row, and so on.
""" *
    **
    ***
    ****
"""
""" for row in range(4):
    for col in range(row+1):
        print("*",end='')
    print('') """

# Q3. Print two stars in first row, four stars in second row, and so on.
""" **  2*1
    ****   2*2
    ******   
    ******** 
    """
""" n=4
for row in range(1,n+1):
    for col in range(row*2):
        print("*",end='')
    print('') """

#Q4. Print a reverse right-angled triangle of stars.
""" 
*****
****
***
**
*
"""
""" for row in range(5):
    for col in range(5-row):
        print("*",end='')
    print('') """

#Q6. Print a right-angled triangle of numbers where the number of columns in each row equals the row number.
1
12
123
1234
12345

""" for row in range(5):
    for col in range(1,row+1):
        print(col ,end='')
    print('') """

#Q6. Generate a 5x5 matrix where each cell contains the product of its row and column indices. So the cell on 3rd row and 4th column will have 12.
# Variation : Generalise this to any NxN matrix and take N as input from the user.

""" for row in range(1,5+1):
    for col in range(1,5+1):
        print([row*col],end='')
    print('') """

# Take the size of the matrix (N) as input from the user
""" N = int(input("Enter the size of the matrix (N): "))

# Generate the NxN matrix
for row in range(1, N+1):  # Rows from 1 to N
    for col in range(1, N+1):  # Columns from 1 to N
        print(f"{row * col:5}", end='')  # Product of row and column indices, formatted for alignment , 5 spaces after each number
    print('')  # Move to the next line after each row """

#Q7. Generate an NxM matrix (user inputs N and M) where each cell contains the sum of its row and column indices.

""" N = int(input("Enter the size of the matrix (N): "))
M=int(input("Enter the size of the matrix (M): "))
for row in range(1, N+1):  # Rows from 1 to N
    for col in range(1, M+1):  # Columns from 1 to N
        print(f"{row + col:5}", end='')  # Product of row and column indices, formatted for alignment , 5 spaces after each number
    print('') """

#Q8. Print a multiplication table for numbers 1 to 10 using nested loops.
# Hint: Use an outer loop for rows (numbers 1–10) and an inner loop for columns (1–10).

""" for row in range(1,11):
    for col in range(1,11):
        print(f'{row*col:4}',end='')
    print('') """

#Q9. Given a list of lists, print all the numbers one by one.
# Example: For [[1, 5], [7, 4], [5, 9]], the output should be:
# 1
# 5
# 7
# 4
# 5
# 9
""" list1=[[1, 5], [7, 4], [5, 9]]
for row in range(len(list1)):
    for col in range(len(list1[row])):
        print(list1[row][col]) """

#Q10. Given a list of lists, print the squares of the numbers one by one.
# Example: For [[1, 5], [7, 4], [5, 9]], the output should be:
# 1
# 25
# 49
# 16
# 25
# 81

""" list1=[[1, 5], [7, 4], [5, 9]]
for row in range(len(list1)):
    for col in range(len(list1[row])):
        print((list1[row][col])**(2)) """

#Q11. Flatten a list of lists into a single list.
# Example: Convert [[1, 2], [3, 4]] into [1, 2, 3, 4].

""" list1=[[1, 2], [3, 4]]
list2=[]
for row in range(len(list1)):
    for col in range(len(list1)):
        x=(list1[row][col])  # Output: 1 2 3 4
        list2.append(x)
print(list2) """

#Q12. Given a list of lists, print the factorials of the numbers one by one.
# Hint : Define a separate factorial function and call it from inside the loop.
# Example: For [[1, 5], [7, 4], [5, 9]], the output should be:
# 1
# 120
# 5040
# 24
# 12
# 0
# 362880

""" list1=[[1, 2], [3, 4]]
for row in range(len(list1)):
    for col in range(len(list1)):
        x=(list1[row][col])
        fact=1
        for i in range(1,x+1):
            fact=fact*i
        print(fact) """

#Q13. Given a list of lists, find the sum of all elements.
# Example: For [[1, 2], [3, 4], [5, 6]], the sum is 21.
# Hint : You will need to initialise the sum variable carefully. Where will you initialise it? Outside both loops or inside one of them?

""" list1=[[1, 2], [3, 6]]
# sum=0
for row in range(len(list1)):
    # sum=0  yha kroge tab last wala list sum hoga sirf 😊
    for col in range(len(list1)):
        x=(list1[row][col])
        sum+=x
print(sum) """

#Q14. Given a list of lists, find the sum of all elements of each individual list.
# Example: For [[1, 2], [3, 4], [5, 6]], the output should be:
# 3
# 7
# 11
# Task : Carefully think about the difference between this and the previous problem, in terms of where to initialise the sum variable.

""" list1=[[1, 2], [3, 6]]
for row in range(len(list1)):
    sum=0 # yha kroge tab last wala list sum hoga sirf 😊
    for col in range(len(list1)):
        x=(list1[row][col])
        sum+=x
    print(sum) """

#Q15. Given a list of lists, print the number of even numbers in each individual list. 
# Example: For [[1, 2], [3, 4, 10, 12], [8, 6]], the output should be:
# 1
# 3
# 2
""" list1=[[1, 2], [3, 6],[2,2,2,7]]
for row in range(len(list1)):
    count=0
    for col in list1[row]:
        if col%2==0:
            count+=1
    print(count) """
