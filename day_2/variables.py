#Day 2: 30 Days of python programming

#Ex 1

first_name = 'cesar'
last_name = 'castillo'
full_name = 'cesar castillo'
country = 'mexico'
city = 'mexico city'
age = 35
year = 2023
is_married = True
is_true = True
is_light_on = True

is_has_job, job_name, working_hours = True, 'Data Nerd', 5

#Ex 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print('Tamaño : ',len(first_name))
print('Tamaño : ',len(last_name))

#A4
num_one = 5
num_two = 4

total = num_one + num_two
diff = num_two - num_one
product =  num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print('total : ', total)
print('diff : ', diff)
print('product : ', product)
print('division : ', division)
print('remainder : ', remainder)
print('exp : ', exp)
print('floor_division : ', floor_division)

#A5 Radius of a circle is 30 m
radius = 30
vpi = 3.14
area_of_circle = vpi * (radius ** 2)
print('Area del circulo : ',area_of_circle)
circum_of_circle = vpi * (radius * 2)

radius = input('Write de radius of a circle : ')
area_of_circle = vpi * (int(radius) ** 2)
print('Area del circulo : ',area_of_circle)

#A6
first_name = input('Teclea la variable first_name: ')
last_name = input('Teclea la variable last_name: ') 
full_name = input('Teclea la variable full_name: ') 
country = input('Teclea la variable country: ') 
age = input('Teclea la variable age: ') 

#A7
help['keywords']