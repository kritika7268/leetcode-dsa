#Find the least common multiple of two numbers.
#Sample Input: 12 18
#Sample Output:36
a, b = map(int, input("Enter numbers: ").split())
x, y = a, b
while y != 0:
    x, y = y, x % y
gcd = x
lcm = abs(a * b) // gcd
print(lcm)
