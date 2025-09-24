# # Bitwise left shift :
# # the << inserts the specified number of 0's from the right 
# #and same amount of leftmost bits falloff if it is 0's

# #start with 1's
# # 1001001011
# # 100100101100000

# #starts with 0's
# #0000000000011    3  => 3<<2
# #0000000001100    12


# # <<2
# # <<5
# # <<4

# a=int(input())
# print(a<<2)
# print(bin(a))

# # 1010   ->10
# # 101000   ->40

# # Bitwise right shift :
# # the >> inserts the specified number of 0's from left to right  
# #Empty bits at left side are filled with 0's

# a=int(input())
# print(a>>3)
# print(bin(a))


# # 1100  ->12
# # 0011  ->3

# # 101000  ->40
# # 001010  ->10

# # 60>>3 =>7

# #111100     ->60
# #000111     ->7

# print(bin(7))


# Assignment operators:

# ->the assignment operators are used to assign the values to the variables

# ->we can use the assignment operator along with arithmetic and bitwise operators


# a = 10
# print(a)

# # using assignment operator along with Arthimetic operators
# a+=5
# print(a) 
# a-=5
# print(a) 
# a*=5
# print(a)
# a/=5
# print(a)
# a%=5
# print(a)
# a//=5
# print(a)
# a**=5
# print(a)

# # using assignment operator along with bitwise operators
# b = int(input())
# print(b)

# b&=5
# print(b)
# b|=5
# print(b)
# b^=5
# print(b)
# b<<=5
# print(b)
# b>>=5
# print(b)



# #Swapping of 2 numbers

# #By using temporary variables
# a=10
# b=20
# temp =a
# a=b
# b =temp
# print(a)
# print(b)

# #without using temporary variable 
# #using addition and subtraction operators
# a=10
# b=20
# a=a+b   #30
# b=a-b   #30-20 ->10
# a=a-b   #30 -10 ->20
# print(a)
# print(b)

# #By interchanging the variables

# a=10
# b=20
# a,b=b,a
# print(a)
# print(b)

# # By using Bitwisr XOR operator
# a=10
# b=20
# a=a^b
# b=a^b
# a=a^b
# print(a)
# print(b)

# #by using multiplication and Division operators
# a=10
# b=20
# a=a*b   #200
# b=a//b  # 200//10 => 20
# a=a//b  # 200//20 => 10
# print(a)
# print(b)


