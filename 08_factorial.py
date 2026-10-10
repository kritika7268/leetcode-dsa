#Find the factorial of a given number N.
#Sample Input: 5
#Sample Output: 12
n=int(input("Enter a number: "))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)