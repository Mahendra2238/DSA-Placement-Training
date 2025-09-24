#  #python basics
# #oops concepts
# #language converters - Assembler, compiler, interpreter

# import time
# a=18
# b="Mahendra singh dhoni"
# print(a)
# print(type(a))
# print(''' type(a)\n''')
# # no multiline comment in python we have to use # and space for each line we can convert into string without printing using ''' or """ 

# #print(*objects,sep=' ',file=sys.stdout,flush=False)
# '''for i in range(5):
#     print(i,end="-",flush=True)    #end-same line  sep-new line
#     time.sleep(2) '''

# # Escape sequences   / - forward slash  \ - backward slash
# print('Mahendra singh\n dhoni')
# print('Mahendra singh\t dhoni')  #1 tab = 4 (to 5) spaces
# print('Mahendra singh\\ dhoni')
# print('Mahendra singh\' dhoni\'')
# print('Mahendra singh\? dhoni\n')

# #Decimal precision
# print('Hemanth')
# print("Hemanth"[0])
# print("Hemanth"[-1]) #last char
# print("%s"%"Hemanth") #format specifier
# print("%2s"%"Hemanth")
# print("%.2s"%"Hemanth") #use this concept in captcha, otp, search, password etc
# print("%7.3s"%"Hemanth") #out of 7, 3 char will print nd remaining 4 are spaces
# print("%-7.4s"%"Hemanth")

# #integer format specifier
# print("\n%d" %10) #decimeal integer
# print("%i" %10) # signed " "
# print("%5d" %1000)
# print("%-5d" %1000)
# print("%.05d" %10)

# #float
# print("%f"%10) #after decimal 6 0's
# print("%.2f"%20)
# print("%6.2f"%10)

# import keyword
# print(keyword.kwlist)

# #A formatted string literal or f-string is a string literal that is prefixed with f or F.
# # These strings may contain replacement fields, which are expressions delimited by curly braces {}.
# # While other string literals always have a constant value, formatted strings are really expressions evaluated at run time.
# a=10
# print(f"{a:5}")
# b=10.66
# print(b)
# print(f"{b:.5f}")
# print(f"{b:.4f}")
# print(f"{'Hello':10.4}9")

# # variable is a name for any memory location which is used to tore the value for temperory purpose
# # ways to initialize a variable
# d=10
# a,b=10.6,20
# c=[1,2,3]
# print(type(d))
# print(type(a))
# print(type(c))

# #datatypes - int,float,string,boolean
# a=2+4j
# print(type(a))

# # different ways to print
# name="virat"
# Number=18
# print(name,Number)
# print(name+" "+str(Number))  #concat
# print("Name: "+name+"\nNumber: "+str(Number))
# print("Name:{},Number:{}".format(name,Number))
# print("Name:{0},Number:{0}".format(name,Number))
# print("Name:{1},Number:{0}".format(name,Number))
# print("Name:{a},Number:{b}".format(a=name,b=Number))
# print("Name:%s,Number:%d"%(name,Number))

# # Types of operators:
# # arithmetic,relational/comparision,logical,assignment,bitwise
# # other 2 special operators in python - 
# Membership-in,not in (membership operators test for the membership of an object in a sequence, such as strings, lists, or tuples),
# # An alternative to Membership ‘in’ operator is the contains() function syntax: operator.contains(sequence, value) eg: print(operator.contains([1, 2, 3, 4, 5], 2))
# # Identity -  Identity Operators are used to compare the objects if both the objects are actually of the same data type and share the same memory location.
# # is and is not  (The equality operator '==' is used to compare the value of two variables, whereas the identities operator is used to compare the memory location of two variables.)
# # Assignment op - simple and compound assignment

# # ASCI value of a-z -> 97 to 122
# # A-Z -> 65 to 90
# # 0-9  -> 48 to 57

# # Bitwise op - &, |, ^, <<, >>, ~ 
# Introduction to python programming:

# ->python is a most popular
# ->purely object oriented programming language
# ->Guido van Rossum was developed python
# ->released to the public in 1991

# used in
# ->web development
# ->software development
# ->data science

# why we need programming
# -> used to get faster and accurate result
# ->used to communicate with the machines

# machine only knows binary language

# Binary language - low level language

# 0 and 1

# programming language -> High level language

# translator -> who knows both the languages

# ->complier
# 	->it will execute all the instructions at a time


# #properties used to develop a program:

# ->Alphabets(A-Z)(a-z)
# ->Digits(0-9)
# ->special symbols
# ->white spaces

# Tokens:

# ->A token is nothing but smallest individual unit

# ->keywords
# ->identifiers
# ->operators
# ->literals
# ->punctuators


# #include <stdio.h>

# int main()
# {
#     printf("Hello World");
#     int a=10;
#     printf("\n%d",b); //error
#     return 0;
# }

# ->interpreter
# 	->it will execute the line by line
# a=10
# print("Hello world")
# print("Hello world")
# print("Hello world")
# print(b)

# Variables :
# In Python, variables are used to store data values that can be referenced and manipulated throughout a program. A variable acts as a container for data. The data stored in a variable can be of different types, such as integers, floats, strings, lists, dictionaries, etc.

# Data types :
# int, char,float,double,list,tuple,set,Dictionary

# a=18
# print(type(a))
# print(id(a))


# print((a));
# Input and Output statements:


# Output statements:
# ->used to print the output to the console

# Syntax:

# print(*objects,sep='',end='',file=sys.stdout,flush=False)


# #Objects -> we can give any no.of objects seperated by commas
# a,b=10,40
# print(a,b)

# # sep => is used to print multiple items with a separator

# print("python","java","c",sep="||")

# #end => by usign end we can change the end character
# # -> by default the value of end character is new line

# print("Hello",end=" ")
# print("World")

# # ->file ->to print the output in other files
# #  By default sys.stdout which is nothing but console

# # ->flush - > print with a delay between the output 
# # default value is false

# import time
# for i in range(5):
#     print(i,end=" ",flush=True)
#     time.sleep(1)

# import math
# print(math.pi*10)

# # Escape sequence charecters
# # \n-> nwe line output
# # \t ->tab space
# # \\ ->Backslash
# # \v =>vertical tab space


# print("Hello\nWorld")
# print("Hello\tWorld")
# print("Hello\\World")
# print("Hello\vWorld")


# # print hello world within double qoutes
# print("\"Hello world\"")

# print("\'Hello world\'")


# # Input statements

# a = input()
# print(a)
# print(type(a))

# c=int(input())
# print(c)
# print(type(c))

# b=float(input())
# print(b)
# print(type(b))

# # ->the type operator is used to check the type of the variable or object



# # Comments

# # -> 2 types of Comments

# # ->single line Comments
# # ->Multi line Comments

# # ->to represent comments we have to use hash(#) symbol for both single and multi line comments

# # Note: ->in python we can place comment in string without assinging that to any variable
# # in this case we have to use single tripe Quotes or double triple Quotes

# '''
# This is about comments
# '''

# """
# we can use single tripe Quotes or double triple Quotes
# """


# # Decimal precison



# print("Hello")
# print("Hello"[0])
# print("Hello"[-1])


# #string format specifiers

# print("%s"%"Hello")
# print("%2s"%"Hello")    #minimum field width is 2 charecters
# print("%10s"%"Hello")   #minimum field width is 10 charecters so that it leaves number - length of string spaces
# print("%.2s"%"Hello")   #limits the string to a maximum of 2 charecters
# print("%.7s"%"Hello")   #limits the string to a maximum of 7 charecters
# print("%10.3s" % "Python")   # Field width 10, but limits to 3 characters, so 7 leading spaces
# print("%-10.3s" % "Hello")   # Field width 10, but limits to 3 characters, so 7 trailing spaces


# #character format specifiers

# print("%c" % 65)          # Prints the ASCII character for 65 ('A')
# print("%c" % 'B')         # Prints the character itself ('B')
# print("%5c" % 'A')        # Field width of 5
# print("%-5c" % 'A')       # Left-align character in a field of 5

# //integer format specifier

# print("%d" % 10)       # Decimal integer
# print("%i" % 10)       # Signed integer
# print("%5d" % 10)      # Minimum field width of 5
# print("%.5d" % 10)     # Pads with zeros to ensure 5 digits
# print("%+d" % 10)      # Adds a '+' sign for positive numbers
# print("%+d" % -10) 
# print("%+d" % --10) 
# print("%+d" % -10) 
# print("%-5d" % 10)     # Left-aligns the number in a field of 5
# print("%05d" % 10)     # Pads with zeros to fill width of 5

# //floating format specifiers

# print("%f" % 10)        # Default floating-point representation
# print("%10f" % 10)      # Minimum field width of 10
# print("%.1f" % 10)      # 1 digit after the decimal point
# print("%.2f" % 10.1234) # 2 digits after the decimal point
# print("%10.3f" % 10)    # Field width 10, 3 digits after decimal
# print("%-10.2f" % 10)   # Left-align with 2 decimal places
# print("%e" % 10)        # Scientific notation (lowercase e)
# print("%E" % 10)        # Scientific notation (uppercase E)
# print("%g" % 10.1234)   # General format (shorter of %f or %e)
# print("%G" % 10.1234)   # General format (shorter of %f or %E)

# # print(f"{variable:widthpresicion}") ->it will check for n digits in the output
# # ->if it's less than it will add spaces infront of given digit

# a=10
# print(a)   #10
# print(f"{a:5}")    # output:   10

# print(f"{a:05}")    #output:00010

# b=10.053
# print(b)

# print(f"{b:10.8f}")

# print(f"{'Hello':10.4}")


# # for any float number we will be having 6 deciaml places

# a=10.5536
# print("%f"%(a))

# b=50000.56767345
# print("%.2f"%(b))



# ->Keywords

# # Keyword are nothing but reserverd words or inbuilt words
# # each keyword has its own functionality
# # we can't use keywords as variable names
# # all keywords are in lowercase except True , False , None

# import keyword
# print(keyword.kwlist)


# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del',
#  'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 
# 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']




# # identifiers

# # ->identifiers are nothing but name given to a variable , function,class,module etc
# # ->the identifier should be written with a combination of charecters,Digits and underscores
# # ->To write the identifir=ers we are having specific set of rules

# # ->the identifier will have to start with charecter or underscore 
# # ->we can't start the identifier with a digit
# # ->identifier should be a keyword
# # ->identifiers are case-sensitive
# # ->white spaces are not allowed
# # ->we can't use any special symbol except underscore(_).


# a=10
# print(a)

# _begin ="Hello"
# print(_begin)

# # 23osr = 46        #Invalid
# # print(23osr)

# _45 ="wrt"
# print(_45)

# abc%b = "123"
# print(abc%b)    #Invalid


# # Varibles

# # -> A variable is a name which is given to memory location
# # which will stores the value temporarily

# # Single assignment

# a=10
# print(a)

# # multiple assingment

# a,b=45,"Hello"
# print(a,b)

# # Assigning a single value to multile varaibles
# c=d=e=345
# print(c,d,e)

# c=[3,4,5]
# print(type(c))===list

# # if we are assgning  multiple values to a single variable 
# # it should be treated as tuple
# a=120,240,560
# print(a)

# b=345,
# print(b)


# #Datatypes

# # int
# # float
# # String
# # boolean

# a = 10
# print(a)
# print(type(a))

# b = 10.567856
# print(b)
# print(type(b))

# # complex number

# a = 2+4j
# print(a)
# print(type(a))

# c = "python"
# print(c)
# print(type(c))

# d = True
# print(d)
# print(type(d))


# # value
# # type of the data
# # memory location

# a = 10
# print(a)
# print(type(a))
# print(id(a))


# # print statement using format strings

# print("Hello world")

# a=10
# b=40
# print(a,b)

# name = "Python"
# year = 1991
# print(name,year)

# # using , to separtae strings and variables

# print("language:",name,"Release:",year)

# # string and variable concatination

# print("language:"+name+"Release:"+str(year))

# # Format strings

# print(f"language:{name},Release:{year}")

# print("language:{},Release:{}".format(name,year))

# print("language:{0},Release:{1}".format(name,year))

# print("language:{1},Release:{0}".format(year,name))


# print("language:{a},Release:{b}".format(a=name,b=year))


# print("language:%s ,Release:%d"%(name,year))

# Operators:

# operator is nothing but a symbol

# % > + = - => operator

# which is used to operate the operands

# operand -> value or variable

# 34 , a , num , 55  =>operands


# by using operators we can perform operations on values or variables

# collection of values along with operators and variables is nothing but an expression

# ->we can assign a value to a variable
# ->we can assign a variable to a variable
# ->we can assign an expression to a variable


# ->a=10
# ->b=10

# ->c=a
# ->d=b

# ->sum = a+b
# ->diff = a-b


# Types of operators:

# In python there are 7 types of operators

# ->Arithmetic operators
# ->relational operators
# ->logical operators
# ->bitwise operators
# ->Assignment operators
# ->identity operators
# ->membership operators


# ->Arithmetic operators:
	
# 	->arithmetic operators are used to perform operations on numeric values
# 	->by using these operators we can perform common mathematical operations, like 
# like
# 	->Addition -> +
# 	->subtraction -> -
# 	->multiplication -> *
# 	->Division -> /
# 	->Modulo division -> %
# 	->floor Division -> //
# .
# 	->Exponential -> **



# #Addition of 2 numbers

# #By using Additon operator (+)
# a = int(input())
# b = int(input())
# print(a+b)

# 2*4 => 8
# -2*4 => -8
# 2*-4 => -8
# -2*-4 => 8

# #Without using Additon operator
# a=int(input())
# b=int(input())
# print(a-(-b))


# #By using bitwise operators
# a=int(input())
# b=int(input())
# while b!=0:
#     carry = a&b
#     a=a^b
#     b=carry<<1
# print(a)

# #By using functions
# def sum(a,b):
#     print(a+b)
# a=int(input())
# b=int(input())
# sum(a,b)

# #By using compound assignment
# a=int(input())
# b=int(input())
# a+=b
# print(a)

# #By using the sum inbuilt method in lists
# a=int(input())
# b=int(input())
# print(sum([a,b]))

# #By using the inbuilt method in operator module
# import operator
# a=int(input())
# b=int(input())
# print(operator.add(a,b))

# #subtraction of 2 numbers
# a=int(input())	
# b=int(input())
# print(a-b)

# #Multiplication of 2 numbers
# a=int(input())
# b=int(input())
# print(a*b)

# #Division of 2 numbers
# a=int(input())
# b=int(input())
# print(a/b)
# print("%.5f"%(a/b))
# #The output should be returned in float value

# #floor division
# a=int(input())
# b=int(input())
# print(a/b)  #float value
# print(a//b) #integer value
# #The output should be returned in int value

# #Modulo division
# a=int(input())
# b=int(input())
# print(a/b)  #Quoficient with decimal part
# print(a//b) #Quoficient without decimal part
# print(a%b)  #retuns remainder

# # divisor
# #divident
# # Quoficient
# #remainder

# #Exponential operator
# a=int(input())
# b=int(input())
# print(a**b) #=>a power b =>10 power 2  =>100

# #relational operators

# ->relational operators are used to compare 2 values or variables
# ->these operators are also known as comparison operators
# ->by using relational operators we can form simple conditions
# ->the output is in the form Boolean values either True or False

# greater than -> >
# lessthan -> <
# greater than or equal to -> >=
# lessthan or equal to -> <=
# double equal to  -> ==
# not equal to -> !=


#  a>b  ,  a <= b  , a!=b

# ->2 outcomes
# ->weather a is greater
# ->or b is greater

# ->any one of both the outcomes is true

# #Example

# a=int(input())  #10
# b=int(input())  #20
# print(a>b)  # (10>20) Flase  
# print(a<b)  #(10<20) True
# print(a>=b) #(10>=10) Flase
# print(a<=b) #(10<=20) True
# print(a==b) #(10==20) Flase
# print(a!=b) #(10!=20) True


# #Logical Operators:

# ->By using logical operators we can compare 2 simple conditions
# ->and we can form compound conditions 
# ->these operators will returns output in Boolean values weather it is True or False


# logical and  ->and
# logical or  ->or
# logical not  ->not

# logical and:
# ->if both the conditions are true it returns true
# ->otherwise false

# a=int(input())
# b=int(input())
# print(a>b and a>=b)

# logical or:
# ->if both the conditions or false it returns false
# ->otherwise true

# a=int(input())
# b=int(input())
# print(a>b or a==b)

# logical not:
# ->if it is True it will returns False (not True)
# ->if it is False it will returns True (not False)

# a=False
# print(not a) #True


# #Bitwise operators

# ->bitwise operators are used to compare binary bits of 2 numbers

# Bitwise and -> &
# Bitwise or -> |
# Bitwise XOR -> ^
# Bitwise not -> ~
# Bitwise left shift -> <<
# Bitwise right shift -> >>


# bitwise and :

# # if both the bits are 1 then 1 else 0

# a = int(input())    #4
# b = int(input())    #5
# print(a&b)      #4

# # print(bin(4)) #100
# # print(bin(5)) #101
# # 100
# # 101
# # ----
# # 100

# bitwise or :

# # if one or two bits are 1 then 1 else 0

# a = int(input())    #4
# b = int(input())    #5
# print(a|b)      #5