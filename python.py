# print("Hello World")
# print(2)
# print(2<3)
# print(2+5)

#  Variable in python 

# ! cannot start with number (1a = 15)
# ! cannot contain space (a   b = 14)
# ! cannot start with a special character ($a = 45) // can use only underscore (_a = 15)

# a = 10
# print(a)
# b = 10

# print(a , b)

# print(id(a), id ( b))

# c = "hello"
# print(c)

# ? string Concatenation in python 

# a = "hello" 
# b = "world"
# c = 30

# print( a + " " +b)

# print("my name is", a , b)

# print(c + 20)

# print( a + str(c))

# ? operators in python

# ** Arithmetic operators(+ , - , * , / , % , ** , //) 
# a = 10
# b = 20 

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)
# print(5 ** 2)
# print(10 // 3) # !floor division 

# ** Assignment operators( = , += ,  -=)

# x = 5 
# x += 3 # ! x = x + 3
# print(x)
# x -= 3 # ! x = x- 3
# print(x)

# ** Comparision operators(==, != , > , < , >= , <= )

# print(10 == 10)
# print(10 != 10)
# print(20 > 10)
# print(20 < 10)
# print(10 >= 10)
# print(9 <= 10)

# ** Logical operators( and , or , not )

# print(10>=10 and 20<30)
# print(10>10 or 20>30)
# print(not 2>3)

# ** Membership operators ( in , not in)

# str1 = "Hello";    
# print('H' in str1)
# print('h' in str1)
# !print(('h' and 'H') in str1)

# str2 = [10, 20, 30, 40]
# print(50 in str2)
# print(50 not in str2)

# ** Identity operator (is , is not)

# x = 10
# y = 10
# print(x is y, x == y)
# print(x is not y, x != y)

# ** Bitwise operators ( & , | , ^ )

x = 10
y = 8
print(bin(x))         # ?0b1010
print(bin(y))         # ?0b1000
print(x&y , bin(x&y)) # ?0b1000 8 
print(x|y , bin(x|y)) # ?0b1010 10
print(x^y , bin(x^y)) # ?0b0010 2