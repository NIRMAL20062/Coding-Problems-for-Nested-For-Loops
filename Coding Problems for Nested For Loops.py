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

for row in range(5):
    for col in range(1,row+1):
        print(col ,end='')
    print('')

