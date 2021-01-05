1). Swap Numbers
--->  a,b = b,a

2). Reverse a string
---> mystr[::-1]

3). String Palindrom
---> mystr == mystr[::-1]

4). Fibonacci Series
---> fib = lambda x:x if(x <= 1) else fib(x-1) + fib(x-2)

5). Factorial Of a Number
---> fact = lambda n:[1,0][n > 1] or fact(n-1)*n

6). Code to shutdown a computer in python
--->  import os
--->  os.system("shutdown /s /t 1")

7). Code to shutdown a computer in python
---> #include <stdio.h>
     #include <stdlib.h>
     int main(){
     system("c:\\windows\\system32\\shutdown /s");
     return 0;
     }

8). Printing strings pattern in right triangle shape
---> text = "python"
     for index in len(text):
         print(*text[:index + 1])

Output:- p
         p y
         p y t
         p y t h
         p y t h o
         p y t h o n


9). Vibrant circle using tirtle in python
---> import turtle
     t = turtle.Turtle()
     s = turtle.Screen()
     s.bgcolor('black')
     t.pencolor('white')
     a = 0
     b = 0
     t.speed(0)
     t.penup()
     t.goto(0,200)
     t.pendown()
     while(True):
         t.forward(a)
         t.right(b)
         a += 3
         b += 1
         if(b == 210):
             break
        t.hideturtle()
    turtle.down()

10). Library for blazingly fast cleaning swear words (and their leetspeak) in strings.
---> pip install better-profanity
from better_profanity import profanity
profanity.load_censor_words()
text = "You piece of shit"
profanity.censor(text)
text = "...shit...hello_cat_fuck,,,123"
profanity.censor(text)
profanity.censor(text, '-')


11). Instant Map
---> pip install folium
import folium
map = folium.Map(location = [32, 401867,-111,112322])
map.save("map1.html")

12). Python module to convert natural language into ints and floats
---> pip install numerizer
from numerizer import numerize
numerize("five million two thousand five")
op:- '5002005'
numerize("twenty twenty")
op:- '20 20'
numerize("two thousand")
op:- '2000'
numerize("two and three quarter")
op:- '2.75'
numerize("one billion")
'1000000000'

13). Python module that generates fake data for you, whether you need
     to bootstrap your database, create good-looking XML documents, fill-in your persistence to stress test it, or anonymize
     data taken from a production service

---> pip install Faker
from faker import Faker
fake = Faker()
fake.name()
'Anthony Stevenson'
fake.first_name_female()
'Ananda'
fake.user_name()
'barbara77'
fake.password()
'2$v8GK00'
fake.month()
'05'
len(dir(fake))# 300 different methods for your dataset creation :)
300

14). Lightweight web scrapper for python
--->This project is made for automatic web scraping to make scraping easy.
 It gets a url or the html content of a web page and a list of sample
 data which we want to scrape from that page. This data can be text,
 url or any html tag value of that page. It learns the scraping rules
  and returns the similar elements. Then you can use this learned object
   with new urls to get similar content or the exact same element of
   those new pages.
  --> pip install git+https://github.com/alirezamika/autoscraper.git

from autoscraper import AutoScraper
url = "https://stackoverflow.com/questions/2081586/web-scraping-with-python"
wanted_list = ["How to call an external command"]
scraper = AutoScraper()
result = scraper.build(url, wanted_list)
print(result)



15). Diamond Shape pattern
n = 5
for x in list(range(n)) + list(reversed(range(n-1))):
    a = n-x-1
    b = x*2+1
    print('{: <{w1}}{:*<{w2}}'.format('', '', w1 = a, w2 = b))

op:-

      *
     ***
    *****
   *******
  *********
   *******
    *****
     ***
      *


16). Socket Programming
---> How to find IP address of machine. Socket library is
Low-level networking interface in python. You can also find address
of any Website

from socket import gethostbyname
from socket import gethostname
ipAddress = gethostbyname('')
ipAddress
op:- '0.0.0.0'
ipAddress = gethostbyname('www.google.co.uk')
ipAddress
op:- '172.217.163.35'
hostname = gethostname()
ipAddress = gethostbyname(hostname)
ipAddress
op:- '172.18.0.66'


17). Drawing a heart in python
import turtle
juliet = turtle.Turtle()
juliet.color("misty rose")
juliet.width(3)
romeo.color('violet')
romeo.width(3)

romeo_last_name = "montague"

romeo.left(40)
romeo.forward(100)
for side in range(185):
    romeo.forward(1)
    romeo.left(1)
romeo.hideturtle()

if(romeo_last_name == 'montague'):
    juliet.left(140)
    juliet.forward(100)
    for side in range(185)

18). Statistics function in python
from statistics import *
a = [1,3.5,4,6,10,7.3]
mean(a)
op:- 5.3
median(a)
op:- 5.0
median_grouped(a)
op:- 5.5
median_high(a)
op:- 6
median_low(a)
4


19). Unicode strings for characters in python
import unicodedata as uni
uni.name('$')
op:- 'DOLLAR SIGN'
uni.name('*')
op:- 'ASTERISK'
uni.name('')

20). Shift Cipher
---> Shifting characters for encryption in python terminology
import string
alphabets = string.ascii_lowercase
alphabets = "abcdefghijklmnopqrstuvwxyz"
def encrypt(string, shift = 4):
    encrypted_string = ""
    for c in string:
        index = alphabets.index(c)
        shifted_index = (index + shift) % len(alphabets)
        encrypted_string += alphabets[shifted_index]
    return encrypted_string
print(encrypt("pythonlearning"))

op:- tcxlsrpievrmrk


21). Building a Christmas tree
a = 40
b = 0
space = 40
while(b < a-1 and a > 0):
    print(' '*a+'*'+'*'*b)
    a -= 1
    b += 2
for _ in range(4):
    print(' ',*(space-1)+'|||')
print(' '*(space-5), '\_@_@_@_/')


22).
import functools
list1 = [1,2,3,4]
func = lambda x,y:x*y
functools.reduce(func, list1)
op:- ?

23). class MathUtils():
        @staticmethod
        def avg(a,b):
            return a+b/2
    MathUtils.avg(4,5)


24). from timeit import timeit#Check how much time will it take to run particular code with timeit
code = '''
def foo():
    i = 1
    for _ in range(100):
        i += 1
    '''
timeit(stmt = code, number = 100000)
timeit(stmt = code, number = 200000)
timeit(stmt = code, number = 300000)


25).
n = 5
for level in range(1, n+1):
    print(level * '*')

op:-
*
**
***
****
*****
for level in range(1, n+1):
    print(' ', * (n-level) + level * '*')

op:-
    *
   **
  ***
 ****
*****


26).
class Hello():
    def setStr(self, string):
        self.string = string
    def swap(self):
        return self.string[::-1]
    @property
    def swapPro(self):
        return self.string[::-1]
obj = Hello()
obj.setStr("python learning")
obj.swap()# method of Hello
op:- 'gninrael nohtyp'
obj.swapPro # Property of Hello
op:- 'gninrael nohtyp'


27). File Search engine
import os
fileType = '.mp4' #dot(.) is for current directory
anyFile = os.listdir('.')
for file in anyFile:
    if file.endswith(fielType):
        print(file)# mp4 files name in output


28).
alpha = 65
for ind in range(7):
    for jnd in range(ind+1):
        print(chr(alpha), end = ' ')
    alpha += 1
    print()

op:-
A
B B
C C C
D D D D
E E E E E
F F F F F F
G G G G G G G


29).
num = 1
for ind in range(6):
    for jnd in range(ind + 1):
        print(num, end = " ")
        num += 1
    print()
    num = 1

op:-
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6

30). Read different file formats in python with textract
---> pip install textract
from textract import process# read doc/pdf file in python
data = process("sample.doc")# This return file content in bytes
data = process("sample.doc").decode("utf-8")# Change file read content into string type


31). Copy all data from one file to another
with open('pyFile.txt', 'r') as readObj:
    with open('copyFile.txt', 'w') as obj:
        obj.write(readObj.read())

32). Delete all file data in one line
with open('pyFile.txt', 'w') as obj:
    pass

or

open('pyFile.txt', 'w').close()

33).
import re
text = 'python programming language is for Devs'
re.findall("p\w+", text)# \w+ is for getting all characters till space starts or character ends
op:- ['python', 'programming']
text = 'python programming language is for Devspublic'
re.findall("p\w+", text)
op:- ['python', 'programming', 'public']
re.findall("p\w", text)
op:- ['py', 'pr', 'pu']


34).
import re
text = "Dummy python text"
re.sub("m", "-", text)# sub() function is used for replacing multiple values at once unlike replace method
op:- 'Du--y python text'
re.sub("m|t", "-", text)
op:-'Du--y py-hon -ex-'
re.sub("m|t|o", "-", text)
op:- 'Du--y py-h-n -ex-'


35).
key = ['a', 'b', 'c', 'd']
value = [2,5,1,9]
zip(key, value)
op:- Create a zip object
dict(zip(key, value))
op:- {'d': 9, 'b': 5, 'c': 1, 'a': 2}
list(zip(key,value))
op:- [('a', 2), ('b', 5), ('c', 1), ('d', 9)]



36). function called before its declaration/definition throws compile error in c++ but not in c
#include<stdio.h>
int main(){
 foo();
}

int foo(){
printf("Hello");
return 0;
}


37). Below program throws compiler error in c++ but not in c
--->
#include <stdio.h>

int main(void)
{
    int const j = 20;

    /* The below assignment is invalid in C++, results in error
       In C, the compiler *may* throw a warning, but casting is
       implicitly allowed */
    int *ptr = &j;  // A normal pointer points to const

    printf("*ptr: %d\n", *ptr);

    return 0;
}


38).Void pointer in C++ must be explicitly typecasted otherwise it will throw error
--->

#include <stdio.h>
int main()
{
   void *vptr;
   int *iptr = vptr; //In C++, it must be replaced with int *iptr=(int *)vptr;
   return 0;
}

This is something we notice when we use malloc().
Return type of malloc() is void *. In C++, we must explicitly
 typecast return value of malloc() to appropriate type,
 e.g., “int *p = (int *)malloc(sizeof(int))”.
 In C, typecasting is not necessary.


 39). const variable in C++ must be initialized otherwise throws error
 --->

#include <stdio.h>
int main()
{
    const int a;   // LINE 4
    return 0;
}

Line 4 [Error] uninitialized const 'a' [-fpermissive]



40). C++ does strict type checking
--->

#include <stdio.h>
int main()
{
    char *c = 333; # In C++ invalid conversion from int to char
    printf("c = %u", c);
    return 0;
    }



Same program but different results in c vs c++

41).
---> C produces sizeof(int), C++ produces sizeof(char)
Character literal is treated as int in C but character in C++

#include<stdio.h>
int main()
{
  printf("%d", sizeof('a'));
  return 0;
}


42). Types of boolean results are different in C and C++

//output = 4 in C(which is the size of int)
printf("%d", sizeof(1==1));

//output = 1 in C++ (which is the size of boolean datatype)
cout << sizeof(1==1)

43). Printing a particular sentence without using ;
--> printf() returns the total number of characters written to stdout.
--> Therefore it can be used as a condition check in an if condition,
while condition, switch case and Macros.

a). Using if() condition
#include<stdio.h>
{
    if(printf("Channelise the flow of river"))
    {  }
}

b). Using switch case
#include<stdio.h>
int main(){
    switch (printf("Yes we are going to channelise"))
    {   }

}

c). Using while() condition
#include<stdio.h>
int main(){
    while(!printf("Channelise the workflow"))
    {   }
}

d). Using Macros
#include<stdio.h>
#define PRINT printf("Geeks for Geeks")
int main(){
    if(PRINT)
    {   }
}

44). Printing a ; without using semicolon
#include<stdio.h>
int main(){
//ASCII value of ; is 59
if(printf("%c", 59))
{

}
}

45). Printing numbers from 1 to N without semicolon
a). Recursive approach
#include<stdio.h>
#define N 10

int main(int num){
    if(num <= N && printf("%d", num) && main(num + 1))
    {

    }
}

b). Iterative approach
#include<stdio.h>
#define N 10
int main(int num, char *argv[])
{
    while(num <= N && printf("%d", num) && num++)
    {

    }
}
c).
How do these above solutions work?
main() function can receive arguments. The first argument is argument count whose value is 1 if no argument is passed to it. The first argument is always program name.
#include<stdio.h>

int main(int num, char *argv[])
{
   printf("num = %d\n", num);
   printf("argv[0] = %s ", argv[0]);
}

Output:

num = 1
argv[0] = <file_name>


46). printing a particular word without using loop, recursion and
any control structure

#include<stdio.h>
#include<stdlib.h>
int main(){
    printf("Hey");
    system("test");
    return 0;
}


47). Printing Even number or odd number without using loop
---> Python
arr = ["Even", "Odd"]
print("enter the number")
num = input()
print(arr[int(num) % 2])

---> C++
#include<iostream>
#include<conio.h>

using namespace std;

int main()
{
char arr[2][5] = {"Even", "Odd"};
int num;
cout << "Enter a number: ";
cin >> num;
cout << arr[num%2];
getch();
return 0;
}


48). Python GUI
49). Python Turtle Graphics

50). Class Method vs Static method in python

51). Difference between *args and **kwargs in python
*args(Non-Keyword argument) and **kwargs(keyword arguments)
are the special symbols used for passing variable number of arguments
to a python function.(GFG)

52). Creating and updating PowerPoint Presentation in python using python-pptx
(https://www.geeksforgeeks.org/creating-and-updating-powerpoint-presentations-in-python-using-python-pptx/?ref=rp)


53). Enumerate() in python
---> Enumerate() == iterator count
---> Enumerate() method/function adds a counter to an iterable and returns
it in a form of enumerate object.
(https://www.geeksforgeeks.org/enumerate-in-python/?ref=leftbar-rightbar)



54). Checking if two words are anagram
a).
from collections import Counter
def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)

b).
def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

print(is_anagram('geek', 'eegk'))# True
print(is_anagram('geek', 'peek'))# False


55). Checking the memory usage of an object
import sys
x = 1
print(sys.getsizeof(x))


56). Find the most frequent value in a list
lst = [1,2,3,4,2,2,3,1,4,4,4]
print(max(set(lst), key = lst.count))


57). Returning multiple values from functions
def func():
    return 1,2,3,4
a,b,c,d = func()
print(a,b,c,d)

op:- 1 2 3 4

58).Printing the file path of imported modules
import os
import socket

print(os)
print(socket)


59). Creating a single string from all the elements in list
a = ["Geeks", "for", "Geeks"]
print(" ".join(a))

op:- "Geeks for Geeks"


60). Printing more than one list's items sumultaneously

list1 = [1,3,5,7]
list2 = [2,4,6,8]
# Here zip() function takes two equal length list and merge them
#together in pairs
for a, b in zip(list1, list2):
    print(a, b)

op-
1 2
3 4
5 6
7 8


61). Conversion of string input into list
formatted_list = list(map(int, input().split()))
print(formatted_list)

ip- 2 4 6 8
op-[2, 4, 6, 8]

62). Convert list of list into single list
import itertools
geek = [[1,2], [3, 4], [5, 6]]
lst = list(itertools.chain.from_iterable(geek))
print(lst)

op- [1,2,3,4,5,6]
