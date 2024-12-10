# Print a rectangle of stars (*) with 4 rows and 6 columns.
""" Hint: Use an outer loop for rows and an inner loop for columns.
                ******
                ******
                ******
                ****** 
"""
for row in range(4):
    for col in range(6):
        print("*" ,end=" ")
    print("")