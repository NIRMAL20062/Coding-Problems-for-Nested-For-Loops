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