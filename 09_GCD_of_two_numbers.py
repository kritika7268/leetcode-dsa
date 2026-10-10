#Find the greatest common divisor of two numbers.
#Sample Input: 24 36
#Sample Output: 12
a, b = map(int, input("Enter numbers: ").split())
while b != 0:
    a, b = b, a % b
print(a)