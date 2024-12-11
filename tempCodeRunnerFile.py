def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

list1=[[1, 2], [3, 6],[2,2,2,7]]
for row in range(len(list1)):
    count=0
    for col in list1[row]:
        if is_prime(col):
            count+=1
    print(count)