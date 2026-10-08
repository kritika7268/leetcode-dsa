#2. Palindrome Number
#Given an integer N, check whether it is a palindrome.
#Sample Input: 121
#Sample Output: Palindrome
n=int(input("Enter an integer: "))
original_num=n
reversed_num=0
while n>0:
    digit=n%10
    reversed_num=reversed_num*10+digit
    n=n//10
if original_num==reversed_num:
    print("Palindrome")
else:
    print("Not a Palindrome")