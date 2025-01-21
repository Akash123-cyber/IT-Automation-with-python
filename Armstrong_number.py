##armstrong number
##Armstrong number whose sum of digits raise to the {power==(no. of digits in the number)} equals to 
### the number itself 

x=int(input("enter the number: "))
l=len(str(x))
k=0
n=x
for i in range(l):
    r=x%10
    k=k+r**l
    x=x//10
if k==n:
    print("{} is an armstrong number".format(n))
else:
    print("{} is not an armstrong number".format(n))










