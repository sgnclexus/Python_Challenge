print(True)
print(False)

# Arithmetic Operations in Python
# Integers

print('Addition : ', 1 + 2)
print('Subtraction : ', 2 - 1)
print('Multiplication : ', 2 * 1)
print('Division : ', 4 / 2)
print('Division : ', 6 / 2)
print('Division : ', 7 / 2)
print('Division without the remainder : ', 7 // 2)
print('Division without the remainder : ', 7 // 3)
print('Modulus : ', 3 % 2)
print('Exponentiation : ', 2 ** 3)

# Example: Floats

print('FLoating Point Number, PI ', 3.14)
print('FLoating Point Number, gravity ', 9,81)

# Example: Complex Numbers

print('Complex number : ', 1 + 1j)
print('Multiplying complex numbers : ', (1+1j)*(1-1j))

# Declaring the variable at the top first

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponentiation = a ** b

# I should have used sum instead of total but sum is a built-in function - try to avoid overriding built-in functions
print(total) # if you do not label your print with some string, you never know where the result is coming from
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponentiation)

print('== Addition, Subtraction, Multiplication, Division, Modulus ==')

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)

# Calculating area of a circle
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')                         # Adding unit to the weight

# Calculate the density of a liquid
mass = 75 # in Kg
volume = 0.075 # in cubic meter
density = mass / volume # 1000 Kg/m^3


# Comparison Operators

print(3 > 2)
print(3 >= 2)
print(3 < 2)
print(2 < 3)
print(2 <= 3)
print(3 == 2)
print(3 != 2)

print(len('mango') == len('avocado'))
print(len('mango') != len('avocado'))
print(len('mango') < len('avocado'))
print(len('milk') != len('meat'))
print(len('milk') == len('meat'))
print(len('tomato') == len('potato'))
print(len('python') == len('dragon'))

# Comparing something gives either a True or False

print('True == False', True == True)
print('True == False', True == False)
print('True == False', False == False)

# Other comparison operators

print('1 is 1 ', 1 is 1)                # True - because the data values are the same
print('1 is 1 ', 1 is not 2)                # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh')                # True - A found in the string 
print('B in Asabeneh', 'B' in 'Asabeneh')                # False - there is no uppercase B
print('coding' in  'coding for all')                # True - because coding for all has the word coding
print('a in an ', 'a' in 'an')                # True 
print('4 is 2 ** 2', 4 is 2 ** 2)                # True 

# Logical Operators

print(3 > 2 and 4 > 3)      # True - because both statements are true
print(3 > 2 and 4 < 3)      # False - because the second statement are false
print(3 < 2 and 4 < 3)      # False - 
print('True and True : ', True and True)        # True
print(3 > 2 or 4 > 3)      # True - because both statements are true
print(3 > 2 or 4 < 3)      # True - 
print(3 < 2 or 4 < 3)      # False -
print('True or False : ', True or False)        # True
print(not 3 > 2)      # False - because 3 > 2 is true, the not true gives False
print(not True)      # False -  Negation, the not operator turns true to false
print(not False)      # True -  Negation, the not operator turns true to false
print(not not True)      # True
print(not not False)      # False


#Exercises
#a1
myage = 37

#a2
myheight = 80.0 

#a3
complex_number = 8j

#a4
base = input('Enter base :')
height = input('Enter height :')
area = (int(base)*int(height))/2
print('The area of the triangle is :',area)

#a5
sidea = input('Enter side a :')
sideb = input('Enter side b :')
sidec = input('Enter side c :')

perimeter = (int(sidea)+int(sideb)+int(sidec))
print('The perimeter of the triangle is :',perimeter)

#6
lenght = input('Enter lenght :')
width = input('Enter width :')
perimeter = 2*(int(lenght)+int(width))
area = (int(lenght)*int(width))
print('The perimeter of the triangle is :',perimeter)
print('The area of the triangle is :',area)

#a14
text = 'I hope this course is not full of jargon'
if 'jargon' in text:
    print('The text exists')
else:
    print('The text doesnt exists')

#a16
lengthText = str(float(len('python')))
print('The text on lengthText is :', lengthText)


#a20
if int(9.8) == 10:
    print(True)
else:
    print(False)

#a23
lastvalue = 5
value = 1
print('Exponentiation')
while value <= lastvalue:    
    print(value, value**0,value**1,value**2,value**3)        
    value += 1    
    