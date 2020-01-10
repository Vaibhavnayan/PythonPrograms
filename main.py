'''
#addition
num1=10
num2=11.1
sum=num1+num2

print("Sum of {0} and {1} is {2}" .format(num1, num2, sum))

#factorial-- 5!= 5*4*3*2*1

num3 = 1
fact=1

for i in range(1,num3+1):
  fact=i*fact

print(fact)

#factorial one line-- 5!= 5*4*3*2*1

def factorial(num4):
  return 1 if(num4 == 0 or num4 == 1) else num4 * factorial(num4-1)

n = 4
print(factorial(n))


#CI 
def CI(p,r,t):
  cInterest = p*(pow(1+(r/100),t))
  print(cInterest)

CI(1200,5.4,2)


#armstrong
def armstrong(number1):
  sum=0
  for i in range(len(number1)):
    sum +=(pow(int(number1[i]),len(number1)))
  print (sum)
  if(int(number1) == sum):
    print("armstrong")
  else:
    print("Not")

n1= armstrong(str(1234))

#area of circle

def area(r):
  pi=3.14
  return (pi*r*r)

print(area(10))


#primeNum
primeNum= 5
counter=0

for i in range(2,primeNum-1):  
  if(primeNum % i)==0:
    break
  else:
    counter +=1

print(counter)

if(counter>1):
  print("Prime")
else:
  print("Not Prime")

#fibonacci---011235811

a1=0
a2=1
#n= int(input("Enter range: "))
print(a1)
print(a2)
for i in range(2,5):
  a3=a1+a2
  a1=a2
  a2=a3  
  print(a3)


##ascii

character = "a"
print(ord(character))

#guessthewordGame

import getpass

word = getpass.getpass("Player 1, Give the word: ")
clue = input("Clue: ")
print ("Player 2")
guess=""
guess_try=0
while guess != word.lower() and guess_try != 3:
  guess=input("Guess the word: ")
  if guess != word.lower() and guess_try <  3:
    guess_try +=1
    chances= 3- int(guess_try)
    print("Wrong! {0} chances remaining".format(chances))
    if guess_try == 3:
      print("You lost. The word is " + word)
  else:
    print("Correct ! You Won")


##translater

word= input("Enter phrase: ")
new_word=""
for letter in word:  
  if letter in "aeiou":
    new_word = new_word + "*"
  else:
    new_word = new_word + letter
print(new_word)


#sum of n natural numbers
#1+2+3+4+...

sum = 0
number = int(input("Enter the value of n: "))

for i in range(1,number + 1):
  sum = sum + i*i

print(sum)

#2nd method
def squareOfNum(number):
  return ((number*(number + 1)*(2*number + 1))/6)

print(squareOfNum(5))


#sum of array
sum=0
arr=[1,2,3,4]
for i in arr:
  sum=sum+i
print(sum)


#larget element
arr=[5,2,19,4]
largest= arr[0]

for i in range(len(arr)-1):
  if arr[i+1] > largest:
    largest = arr[i+1]
      
print("Max no" , largest)


#rotat[e
a = [1, 2, 3, 4, 5, 6, 7, 8]
n = 1 #index
a.extend(a[0:n])
del a[0:n]
print(a)


#exchange

a = [1, 2, 3, 4, 5, 6, 7, 8]
pos1=int(input("Enter position 1: "))
pos2=int(input("Enter position 2: "))

temp=a[pos1]
a[pos1]=a[pos2]
a[pos2]=temp
print(a)


#remove duplicates

a = ["Hi", "Hello", "Hi"]
word= input("Enter word to remove: ")
a_new=[]
for i in a:
  if i !=word:
    a_new.append(i)
print(a_new)


#cloning
list1=[1,2,2,3,4]
print(list1)
list2=[]
list2.extend(list1)
print(list2)
list2=list(list1)
print(list2)


#count occurences

list1=[1,2,3,4,1,2,1]
for i in range(len(list1)):
  count=0
  for j in range(len(list1)-1):
    if list1[i] == list1[j+1]:
      count+=1
  print("Number: ",list1[i])
  print("count: ", count)

#count occurences 2nd
list1=[1,2,3,1,9,"s",2,3,4,1,2,1]
s=set(list1)
print(s)
for i in s:
  print(i,"count: ", list1.count(i))

#smallest number
list1=[1,2,3,4,1,2,1,9,10,2,1]
list1.sort()
print(list1[0])
print(min(list1))
print(max(list1))

#n largest number

list1=[1,2,3,4,1,2,1,9,10,2,1]
list1.sort()
n=int(input())
tuples

for i in range(n):
  print(list1[-(i+1)])


#capture duplicates
list1=[1,2,3,4,2,1,4,5,231,6,5,5,321,12,3,1,2,3,321,]
list2=[]

for i in range(len(list1)-1):
  for j in range(i+1,len(list1)):
    if list1[i] == list1[j] and list1[i] not in list2:
      list2.append(list1[i])

print(list2)

#break list in n part

list1=[1,23,42,1,3,2,1,1,21,4,1,2,4]
list2=[]
for i in range(0,len(list1),3):
  list2.append(list1[i:i+3])

print(list2)

#palindrome string

s="hello"
s2=s[::-1]
print(s2)
'''

#reverse string
string1 = "hello hi"
print(string1[::-1])

#remove ith pos word

string1="hello"
string2=""

for i in range(0,len(string1)):
  if i!=2:
    string2 = string2 + string1[i]
print(string2)


#check substring presence

string1= "hello hi hey"
string2="hello"

if string2 in string1:
  print("YES")
else:
  print("NO")

#print even length

string1= "Hi I am Python from repl. How are you!"
string2= string1.split(' ')
i=0
print(len(string2))
while i < len(string2):
  if (len(string2[i]) % 2==0):
    print(string2[i])
  i=i+1

#accept only vowel string
'''
s=input("Enter string: ")
if ('a' in s and 'e' in s and 'i' in s):
  print("Accepted")
else:
  print("Rejected")
'''

#print matching string

string1=set("Hellooo")
print(string1)
string2=set("Hellooowa")
print(string2)
string3= string1 & string2

for i in string3:
  print(i)

#count vowels in string

string1="Hellooo"

vowel = set("aieouAEIOU")
counter=0
for i in string1:
  if i in vowel:
    counter +=1
print(counter)

#remove duplicates in string

string1="HHerasllooo"
str2=""
for i in string1:
  if i not in str2:
    str2 = str2+i

print(str2)

#check if a string contains any special character
import re
regex=re.compile('[@#]')
string1="helo!@"
if(regex.search(string1)== None):
  print("accepted")
else:
  print("Not accepted")



#random string generation

import string
import random

string1= string.ascii_lowercase 
string2=random.choice(string1)
print(string2)

#file read and write
import test

print(test.printing())

file1= open("Content.txt","r")

print(file1.read())

file1.close()


#MCQ
from Question import Question

questions=["What color banana is?\n (a) Red (b) Yellow (c) Blue \n", "What color sky is?\n (a) Blue (b) Red (c) Pink\n"]

mcq = [Question(questions[0], "b"),
Question(questions[1], "a")]

def test(mcq):
  score = 0
  for question in mcq:
    ans= input(question.ques)
    if ans == question.ans:
      score +=1      
  print("Your score is: " + str(score))

test(mcq)
