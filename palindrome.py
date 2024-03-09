n=int(input('Enter any number:'))
x=n
rev=0

while n>0:
    rev=rev*10+(n%10)
    n=n//10
if rev==x:
    print('palindrome')
else:
    print('not palindrome')