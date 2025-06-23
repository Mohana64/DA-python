#1.Check if a number is even or odd
a= 35
if a%2==0:
    print("it is a even number")
else:
    print("it is a odd number")
#2.Check if a number is positive, negative, or zero.
a=0
if a>0:
    print("it is a positive number")
elif a==0:
    print("it is zero")
else:
    print("it is a negative number")
#3.Determine if a character is a vowel or consonant
ch='o'
if ch=='a' or ch=='e' or ch=='i'or ch=='o' or ch=='u':
    print("it is vowels")
else:
    print("it is a consonant")
#4.Check if a year is a leap year
year=2020
if year%400==0 or year%4==0 and year%100!=0:
    print("it is a leap year")
else:
    print("it is not a leap year")
#5.Determine a person's stage of life (child, teen, adult, senior) based on age.
age=20
if age<12:
    print("child")
elif age<=20:
    print("teen")
elif age<60:
    print("adult")
else :
    print("senior")
#6.Check if a password meets length criteria (at least 8 characters).
password="1234b99d9k"
if len(password)>=8:
    print("it is strong password")
else:
    print("week password")
#7.Nested if: Check if a number is positive, and if so, whether it's even or odd.
n=-11
if n>0:
    if n%2==0:
        print("it is positive and even number")
    else:
        print("it is positive odd number")
else:
    print("it is a negative number")
#8.Check if two numbers are equal, or if not, determine which is larger.
nu=10
nu1=90
if nu>nu1:
    print("nu is greater")
elif nu1>nu:
    print("nu1 is greater")
else:
    print("both are equal")
#9.Determine if a given letter is uppercase, lowercase, or neither.
l="Mango"
if l.islower():
    print("the letter is lowercase")
elif l.isupper():
    print("it is uppercase")
else:
    print("it is neither upper nor lowercase")
#10.Check if a character is a digit.
c='10'
if c.isdigit():
    print("c is a digit")
else:
    print("it is a character")
#11.If a character is a letter, check if it is uppercase or lowercase.
chr="Mangoose"
if chr.isalpha():
    if chr.islower():
        print("it is a letter in lower")
    elif chr.isupper():
        print("it is letter is upper")
    else:
        print("it is a mix")
else:
    print("it is not a alpha")
#12.Check if a given number ends with digit 5.
number=55
num=str(number)
if num.endswith('5'):
    print("the number ends with 5")
else:
    print("the number doesn't ends with 5")
#13. Determine if a character is a punctuation mark (only check . , ! ?).
ter="!"
if ter=="." or ter==',' or ter=='!' or ter=='?':
    print("it is a punctuation")
else:
    print("it is not a punctuation")
#14.If a number is even, check if it is also divisible by 4.
n=42
if n%2==0:
    if n%4==0:
        print("it is a even number and it is also divided by 4")
    else:
        print("it is a even number but not divisible by 4")
else:
    print("it is a odd number")
#15.Check if a given string starts with a capital letter
b="Pan"
if b[0].isupper():
    print("it starts with upper case")
else:
    print("it starts with lower case")
#16.If a number is positive, check if it is a perfect square of an integer
import math
p=4
p=math.sqrt(p)
if p>0:
    if p==int(p):
        print("it is positive number and also a perfect square")
    else:
        print("it is a positive number but not a perfect square")
else:
    print("it is negative number")
#17.Check if a string is a palindrome
s="pop"
if s==s[::-1]:
    print("it is a palindrome")
else:
    print("it is not a palindrome")
#18.Determine if a string length is odd or even
m="hype"
if len(m)%2==0:
    print("the string length is even")
else:
    print("the string length is odd")
#19.If a character is a digit, check if it's even or odd digit.
o='44'
if o.isdigit():
    m=int(o)
    if m%2==0:
        print("the char is digit and it even number")
    else:
        print("the char is digit and it is odd number")
else:
    print("the char is a string")
#20.Check if a string starts with 'A' and ends with 'Z'
p="alphz"
if p[0]=="A" or p[0]=='a' and p[-1]=='Z' or p[-1]=='z':
    print("the string starts with 'a' and ends with 'z'")
else:
    print("the string doesn't starts with 'a' and ends with 'z")
#21.Check if a given name starts with a vowel
k="apple"
if k[0]in{"A","E","I","O","U","a","e","i","o","u"}:
    print("the name starts with vowel")
else:
    print("the name doesn't start with vowel")
#22. Classify a number by digit count:
numb=98
nu=abs(numb)#abs-absolute value of a number is its distance from 0, regardless of sign.
if nu<10:
    print("it is single digit")
elif nu<100:
    print("it is double digit ")
else:
    print("it is three or more digit")
