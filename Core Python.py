# -*- coding: utf-8 -*-
"""
Created on Sat May 25 20:29:01 2019

@author: haris
"""
"""assigning variables"""
counter=4545
decimel=12.2
strring="hhii"
"""saving mutilple varibales"""
e=f=g=1515
a,b,c=1,2.3,"djhd" 
print(counter,decimel,a,b,c) 
"""printing in next line"""
print( '\n')
print(e,f,g)
"""varibales"""
var=1
var2=22
print(var,var2)
"""deleting variables"""
del var,var2

"""python strrings"""
strr='hello world'
#print(string.count(0))
print(strr)
print(strr[0])
print(strr[0:3])
print(strr[2:])
"""multiply string"""
print(strr*45)
"""concat"""
print(strr+"hiiii")

"""List(starts with [])and dffernett data types,data can be changed"""

list=['abcd',121,2.3]
list1=['dbj',52]
"""concat"""
print(list + list1)
print(list[0])
print(list*2)
"""tuples(starts with () anddifferent data types, datav cannot be changed)"""
tuple1=('dhudh',545,4.52)
tuple2=('fdefd',54,5.3)
print(tuple1+tuple2)
print(tuple1*2)
#tuple1[3]=5555 since tuple cannot be updated but list can be

"""dictionary (hash table with key and value)"""
dict={}
dict['1']="one value"
dict['2']="two value"
dict2={'name':"lola",'age':'35','dept':'sales'}
print(dict['1'])
"""Printing dictionary values and keys"""
print(dict2.keys(),dict2.values())

"""Operators"""

print(a+b)
print(a-b)
print(a*b)
print(a/b)
"""modulo"""
print(a%b) 
"""Eponential"""
print(a**b) 
"""Floor Division"""
print(a//b)

""""Comparison OPerators"""
"""
== If the values of two operands are equal,
then the condition becomes true.
(a == b) is not true.

!= If values of two operands are not equal,
then condition becomes true.
(a != b) is true.

<> If values of two operands are not equal,
then condition becomes true.
(a <> b) is true. This is similar
to != operator.

> If the value of left operand is greater
than the value of right operand, then
condition becomes true.
(a > b) is not true.

< If the value of left operand is less than
the value of right operand, then
condition becomes true.
(a < b) is true.

>= If the value of left operand is greater
than or equal to the value of right
operand, then condition becomes true.
(a >= b) is not true.

<= If the value of left operand is less than
or equal to the value of right operand,
then condition becomes true.
(a <= b) is true.
"""
if ( a == b ):
   print("Line 1 - a is equal to b")
else:
   print ("Line 1 - a is not equal to b")
if ( a != b ):
   print ("Line 2 - a is not equal to b")
else:  
   print ("Line 2 - a is equal to b")
#if( a <> b ):
#   print ("Line 3 - a is not equal to b")
#else:
#   print ("Line 3 - a is equal to b")
if ( a < b ):
   print ("Line 4 - a is less than b")
else:
   print ("Line 4 - a is not less than b")
if ( a > b ):
   print ("Line 5 - a is greater than b")
else:
   print ("Line 5 - a is not greater than b")
if ( a <= b ):
   print ("Line 6 - a is either less than or equal to b")
else:
   print ("Line 6 - a is neither less than nor equal to b")
if ( b >= a ):
   print ("Line 7 - b is either greater than or equal to b")
else:
   print ("Line 7 - b is neither greater than nor equal to b")
   
"""Assignemnet opeartors"""
k=5
j=55
i=0
i = j + k
print ("Line 1 - Vjlue of i is ", i)
i += j
print ("Line 2 - Vjlue of i is ", i)
i *= j
print ("Line 3 - Vjlue of i is ", i)
i /= j
print ("Line 4 - Vjlue of i is ", i)
i %= j
print( "Line 5 - Vjlue of i is ", i)
i **= j
print ("Line 6 - Vjlue of i is ", i)
i //= j
print ("Line 7 - Vjlue of i is ", i)

"""BItwise operators"""
"""
&
Binary AND
Operator copies a bit to the result if it
exists in both operands.
(a & b) = 12
(means 0000 1100)

|
 Binary OR It copies a bit if it exists in either
operand.
(a | b) = 61
(means 0011 1101)
^
 Binary XOR It copies the bit if it is set in one
operand but not both.
(a ^ b) = 49 (means
0011 0001)

~
Binary
Ones Complement
It is unary and has the effect of
'flipping' bits.
(~a ) = -61 (means
1100 0011 in 2's
complement form due
to a signed binary
number.

<<
Binary Left Shift
The left operands value is moved left by
the number of bits specified by the right
operand.
a << 2 = 240
(means 1111 0000)
 
>>
Binary Right Shift
The left operands value is moved right
by the number of bits specified by the
right operand.
a >> 2 = 15
(means 0000 1111)"""
 
x= 60 # 60 = 0011 1100
y = 13 # 13 = 0000 1101
z = 0
z = x & y; # 12 = 0000 1100
print("Line 1 - Vxlue of z is ", z)
z = x | y; # 61 = 0011 1101
print ("Line 2 - Vxlue of z is ", z)
z = x ^ y; # 49 = 0011 0001
print ("Line 3 - Vxlue of z is ", z)
z = ~x; # -61 = 1100 0011
print ("Line 4 - Vxlue of z is ", z)
z = x << 2; # 240 = 1111 0000
print ("Line 5 - Vxlue of z is ", z)
z = x >> 2; # 15 = 0000 1111
print ("Line 6 - Vxlue of z is ", z )


"""logical operators  """
"""
and
Logical AND
If both the operands are true then condition
becomes true.
(a and b) is true.

or
Logical OR
If any of the two operands are non-zero
then condition becomes true.
(a or b) is true.

not
Logical NOT
Used to reverse the logical state of its
operand.
Not (a and b) is false."""
#---------------------------------------
"""membership operators"""
"""
in 
Evaluates to true if it finds a variable in
the specified sequence and false
otherwise.
x in y, here in results in a 1 if x
is a member of sequence y.
not in 
Evaluates to true if it does not finds a
variable in the specified sequence and
false otherwise.
x not in y, here not in results in
a 1 if x is not a member of
sequence y.
"""
m= 10
n = 20
list = [1, 2, 3, 4, 5 ];
if ( m in list ):
 print("Line 1 - m is available in the given list")
else:
 print("Line 1 - m is not available in the given list")
if ( n not in list ):
 print("Line 2 - n is not available in the given list")
else:
 print("Line 2 - n is available in the given list")
m = 2
if ( m in list ):
 print("Line 3 - m is available in the given list")
else:
 print ("Line 3 - m is not available in the given list")
 """
 is 
Evaluates to true if the variables on either side
of the operator point to the same object and
false otherwise.
x is y, here is results in
1 if id(x) equals id(y).
is not 
Evaluates to false if the variables on either
side of the operator point to the same object
and true otherwise.
x is not y, here is
not results in 1 if id(x) is
not equal to id(y)."""
a = 20
b = 20
if ( a is b ):
 print ("Line 1 - a and b have same identity")
else:
 print ("Line 1 - a and b do not have same identity")
if ( id(a) == id(b) ):
 print ("Line 2 - a and b have same identity")
else:
 print ("Line 2 - a and b do not have same identity")
b = 30
if ( a is b ):
 print ("Line 3 - a and b have same identity")
else:
 print ("Line 3 - a and b do not have same identity")
if ( a is not b ):
 print ("Line 4 - a and b do not have same identity")
else:
 print ("Line 4 - a and b have same identity")
 
 
 """Operators precsdence"""
 
 """
 **  Exponentiation (raise to the power)
~ + - Ccomplement, unary plus and minus (method names for the
last two are +@ and -@)
* / % //  Multiply, divide, modulo and floor division
+ - Addition and subtraction
>> << Right and left bitwise shift
& Bitwise 'AND'
^ | Bitwise exclusive `OR' and regular `OR'
<= < > >= Comparison operators
<> == != Equality operators
= %= /= //= -= +=
*= **=
Assignment operators
is is not Identity operators
in not in Membership operators
not or and Logical operators
"""
 a = 20
b = 10
c = 15
d = 5
e = 0
e = (a + b) * c / d #( 30 * 15 ) / 5
print("Value of (a + b) * c / d is ", e)
e = ((a + b) * c) / d # (30 * 15 ) / 5
print("Value of ((a + b) * c) / d is ", e)
e = (a + b) * (c / d); # (30) * (15/5)
print("Value of (a + b) * (c / d) is ", e)
e = a + (b * c) / d; # 20 + (150/5)
print("Value of a + (b * c) / d is ", e)

"""Decision making"""
var = 100
if var == 200:
 print("1 - Got a true expression value")
 print( var)
elif var == 150:
 print ("2 - Got a true expression value")
 print (var)
elif var == 100:
 print ("3 - Got a true expression value")
 print (var)
else:
 print ("4 - Got a false expression value")
 print (var)
 
 """LOOPS"""
 
 """
 while loop
Repeats a statement or group of statements while a given
condition is TRUE. It tests the condition before executing the
loop body.
for loop
Executes a sequence of statements multiple times and
abbreviates the code that manages the loop variable.
nested loops
You can use one or more loop inside any another while, for
or do..while loop """


""" Using else Statemnt with For looP

----
f the else statement is used with a for loop, the else statement is executed
when the loop has exhausted iterating the list.
If the else statement is used with a while loop, the else statement is executed
when the condition becomes false.
----"""
count = 0
while (count < 5):
 print (count, " is less than 5")
 count = count + 1
else:
 print(count, " is not less than 5")
 
 """Single line"""
flag=1
while(flag):
    print("executed") 
    break  #break statement
 
"""for loop"""
for letter in 'Python': 
     print ('Current Letter :', letter)
fruits=['xdwebcj','dwjbxd','dbdj']
for friut in fruits:
    print(friut)
"""iterating using index"""
for findex in range(len(fruits)):
    print("fruits is (by indx)",fruits[findex])

"""Loop Control Statements"""
"""
break statement

Terminates the loop statement and transfers execution to
the statement immediately following the loop.

continue statement
Causes the loop to skip the remainder of its body and
immediately retest its condition prior to reiterating.

pass statement
The pass statement in Python is used when a statement is
required syntactically but you do not want any command or
code to execute.    """

"""Continue stament"""
for letter in 'Python': # First Example
  if letter == 'h':
   continue
  print ('Current Letter :', letter)   
  
"""break Statement"""
for letter in 'Python': 
 if letter == 'h':
   break
 print ('Current Letter :', letter)  
 
"""Pass Statement"""
for letter in 'Python':
 if letter == 'h':
  pass
  print ('This is pass block')
print ('Current Letter :', letter) 



"""----------------numeric FUNC----------------"""
"""
abs(x)
The absolute value of x: the (positive) distance between x and
zero.
ceil(x)

The ceiling of x: the smallest integer not less than x
cmp(x, y)

-1 if x < y, 0 if x == y, or 1 if x > y
exp(x)

The exponential of x: e x
fabs(x)

The absolute value of x.
floor(x)

The floor of x: the largest integer not greater than x
log(x)

The natural logarithm of x, for x> 0
log10(x)

The base-10 logarithm of x for x> 0.
max(x1, x2,...)

The largest of its arguments: the value closest to positive infinity
min(x1, x2,...)

The smallest of its arguments: the value closest to negative
infinity
modf(x)

The fractional and integer parts of x in a two-item tuple. Both
parts have the same sign as x. The integer part is returned as a
float.

pow(x, y)
The value of x**y.

round(x [,n])
x rounded to n digits from the decimal point. Python rounds
away from zero as a tie-breaker: round(0.5) is 1.0 and round(-
0.5) is -1.0.

sqrt(x)
The square root of x for x > 0"""


"""--------------------Random functs-------------------"""
"""
choice(seq)
A random item from a list, tuple, or string.
randrange ([start,] stop [,step])
A randomly selected element from range(start, stop,
step)

random()
A random float r, such that 0 is less than or equal to r and
r is less than 1

seed([x])
Sets the integer starting value used in generating random
numbers. Call this function before calling any other
random module function. Returns None.

shuffle(lst)
Randomizes the items of a list in place. Returns None.

uniform(x, y)
A random float r, such that x is less than or equal to r and
r is less than y
"""

"""Trig funs"""
"""
acos(x)
Return the arc cosine of x, in radians.
 Python
75
asin(x)
Return the arc sine of x, in radians.
atan(x)
Return the arc tangent of x, in radians.
atan2(y, x)
Return atan(y / x), in radians.
cos(x)
Return the cosine of x radians.
hypot(x, y)
Return the Euclidean norm, sqrt(x*x + y*y).
sin(x)
Return the sine of x radians.
tan(x)
Return the tangent of x radians.
degrees(x)
Converts angle x from radians to degrees.
radians(x)
Converts angle x from degrees to radians.
"""

"""-----constants are pi and e-----"""



"""-----------STRINGS TOPIC--------"""
var1="HEllo"
print(var1+"\a  world")  # bell alertsound for \a 
"""Escape Characters in Stings"""
#""" 
#\a 0x07 Bell or alert
#\b 0x08 Backspace
#\cx Control-x
#\C-x Control-x
#\e 0x1b Escape
#\f 0x0c Formfeed
#\M-\C-x Meta-Control-x
#\n 0x0a Newline
#\nnn Octal notation, where n is in the range 0.7
#\r 0x0d Carriage return
#\s 0x20 Space
#\t 0x09 Tab
#\v 0x0b Vertical tab
#\x Character x
#\xnn Hexadecimal notation, where n is in the range
#0.9, a.f, or A.
#"""
"""operators in Strings"""
"""
+ Concatenation - Adds values on either side of
the operator
a + b will give
HelloPython

* Repetition - Creates new strings,
concatenating multiple copies of the same
string
a*2 will give -HelloHello

[] Slice - Gives the character from the given
index
a[1] will give e

[ : ] Range Slice - Gives the characters from the
given range
a[1:4] will give ell

in Membership - Returns true if a character
exists in the given string
H in a will give 1

not in Membership - Returns true if a character
does not exist in the given string
M not in a will give 1

r/R Raw String - Suppresses actual meaning of
Escape characters. The syntax for raw strings
is exactly the same as for normal strings with
the exception of the raw string operator, the
letter "r," which precedes the quotation
marks. The "r" can be lowercase (r) or
uppercase (R) and must be placed
immediately preceding the first quote mark.
print r'\n' prints \n
and print R'\n'prints \n

% Format - Performs String formatting See at next section
"""

"""Format Specifier"""
"""
%c character
%s string conversion via str() prior to formatting
%i signed decimal integer
%d signed decimal integer
%u unsigned decimal integer
%o octal integer
%x hexadecimal integer (lowercase letters)
%X hexadecimal integer (UPPERcase letters)
%e exponential notation (with lowercase 'e')
%E exponential notation (with UPPERcase 'E')
%f floating point real number
%g the shorter of %f and %e
%G the shorter of %f and %E
"""
"""--------String Methods---------"""
"""
1
capitalize()
Capitalizes first letter of string.
2
center(width, fillchar)
Returns a space-padded string with the original string centered to a total
of width columns.
3
count(str, beg= 0,end=len(string))
Counts how many times str occurs in string or in a substring of string if
starting index beg and ending index end are given.
4
decode(encoding='UTF-8',errors='strict')
Decodes the string using the codec registered for encoding. encoding
defaults to the default string encoding.
5
encode(encoding='UTF-8',errors='strict')
Returns encoded string version of string; on error, default is to raise a
ValueError unless errors is given with 'ignore' or 'replace'.
6
endswith(suffix, beg=0, end=len(string))
Determines if string or a substring of string (if starting index beg and
ending index end are given) ends with suffix; returns true if so and false
otherwise.
7
expandtabs(tabsize=8)
Expands tabs in string to multiple spaces; defaults to 8 spaces per tab if
tabsize not provided.
8
find(str, beg=0 end=len(string))
Determine if str occurs in string or in a substring of string if starting
index beg and ending index end are given returns index if found and -1
otherwise.
9
index(str, beg=0, end=len(string))
Same as find(), but raises an exception if str not found.
10
isalnum()
Returns true if string has at least 1 character and all characters are
alphanumeric and false otherwise.
11
isalpha()
Returns true if string has at least 1 character and all characters are
alphabetic and false otherwise.
12
isdigit()
Returns true if string contains only digits and false otherwise.
13
islower()
Returns true if string has at least 1 cased character and all cased
characters are in lowercase and false otherwise.
14
isnumeric()
Returns true if a unicode string contains only numeric characters and
false otherwise.
15
isspace()
Returns true if string contains only whitespace characters and false
otherwise.
16
istitle()
Returns true if string is properly "titlecased" and false otherwise.
17
isupper()
Returns true if string has at least one cased character and all cased
characters are in uppercase and false otherwise.
18
join(seq)
Merges (concatenates) the string representations of elements in
sequence seq into a string, with separator string.
19
len(string)
Returns the length of the string.
20
ljust(width[, fillchar])
Returns a space-padded string with the original string left-justified to a
total of width columns.
21
lower()
Converts all uppercase letters in string to lowercase.
22
lstrip()
Removes all leading whitespace in string.
23
maketrans()
Returns a translation table to be used in translate function.
24
max(str)
Returns the max alphabetical character from the string str.
25
min(str)
Returns the min alphabetical character from the string str.
26
replace(old, new [, max])
Replaces all occurrences of old in string with new or at most max
occurrences if max given.
27
rfind(str, beg=0,end=len(string))
Same as find(), but search backwards in string.
28
rindex( str, beg=0, end=len(string))
Same as index(), but search backwards in string.
29
rjust(width,[, fillchar])
Returns a space-padded string with the original string right-justified to a
total of width columns.
30
rstrip()
Removes all trailing whitespace of string.
31
split(str="", num=string.count(str))
Splits string according to delimiter str (space if not provided) and
returns list of substrings; split into at most num substrings if given.
32
splitlines( num=string.count('\n'))
Splits string at all (or num) NEWLINEs and returns a list of each line with
NEWLINEs removed.
33
startswith(str, beg=0,end=len(string))
Determines if string or a substring of string (if starting index beg and
ending index end are given) starts with substring str; returns true if so
and false otherwise.
34
strip([chars])
Performs both lstrip() and rstrip() on string.
35
swapcase()
Inverts case for all letters in string.
36
title()
Returns "titlecased" version of string, that is, all words begin with
uppercase and the rest are lowercase.
37
translate(table, deletechars="")
Translates string according to translation table str(256 chars), removing
those in the del string.
38
upper()
Converts lowercase letters in string to uppercase.
39
zfill (width)
Returns original string leftpadded with zeros to a total of width
characters; intended for numbers, zfill() retains any sign given (less one
zero).
40
isdecimal()
Returns true if a unicode string contains only decimal characters and
false otherwise.
"""         
 