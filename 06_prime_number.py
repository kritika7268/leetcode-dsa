#Check whether a given number is prime.
#Sample Input: 29
#Sample Output: Prime
n=int(input("Enter a number: "))
if n<2:
    print("Not prime")
else:
    prime=True
    for i in range (2, int(n**0.5)+1):
        if n%i==0:
            prime=False
            break
        if prime:
            print("Prime number")
        else:
            print("Not Prime number")
