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