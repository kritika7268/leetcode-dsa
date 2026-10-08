#3. Sum of Digits
#Find the sum of digits of a given number.
#Sample Input: 9875
#Sample Output: 29
n=int(input("Enter an integer: "))
sum_of_digits=0
while n>0:
    digit=n%10
    sum_of_digits+=digit
    n=n//10
print("Sum of digits:", sum_of_digits)