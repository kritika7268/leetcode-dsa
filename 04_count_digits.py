#4. Count Digits
#Count the number of digits in a given integer.
#Sample Input: 123456
#Sample Output: 6
n = int(input("Enter numbers: "))
count = 0
while n > 0:
    count += 1
    n //= 10
print(count)