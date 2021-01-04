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
