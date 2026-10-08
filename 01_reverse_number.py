#Given an integer N, reverse its digits and print the reversed number.
#Sample Input: 12345
#Sample Output: 5432
n=int(input("Enter an integer: "))
reversed_num=0
while n>0:
    digit=n%10
    reversed_num=reversed_num*10+digit
    n=n//10
print("Reversed number:", reversed_num)