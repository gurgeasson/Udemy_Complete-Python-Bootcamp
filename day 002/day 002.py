# Primitive Data Types


# Subscripting
print("Hello"[0])

# String
print("123" + "345")

# Integer
print(123 + 345)

# Large Integers
print(123_456_789)

#Float
print(123.456)

#Boolean
print(True)
print(False)


# Type Error, Type Checking and Type Conversion


len("1234")
print(type("1234"))
print(type(1234))
print(type(1234.5))
print(type(True))

# Type Casting
print(int("123") + int("456"))
float()
str()
bool()

name = input("enter your name\n")
lenght_of_name = len(name)
print("number of letters in your name: " + str(lenght_of_name))


# Mathematical Operations


# addition +
# substraction -
# multiplication *
# division /
# floor division //
# to the power **
# modulus %

# code is evaluated left to right - but assignments right side first


# Number Manipulation and F Strings


# Rounding
float_with_too_many_decimals = 3.1415926535897
print(round(float_with_too_many_decimals, 7))

# F Stirngs
# does the conversion to string automatically

not_string = 123
print(f"The value of not_string is: {not_string}")