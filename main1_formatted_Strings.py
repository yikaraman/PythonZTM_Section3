#constants
PI = 3.14

#dunder variables
__hihi = 'hi' # not good practice
a,b,c = 1,2,3
print(a)
print(b)
print(c)


iq = 100
user_age = iq / 5
print(user_age)

#Augmented Assignment Operator

counter = 0

counter += 1
counter += 1
counter += 1
counter += 1
counter -= 1
counter *=2

#Before you click RUN, guess what the counter variable holds in memory!
print(counter)


#Strings
username = "supercoder"
password = 'mypassword'

long_string = '''

WOW
O O
---

'''

print(long_string)

first_name = 'ilker '
last_name = 'kara'

fullname = first_name + last_name
print (fullname)

#String concatenation
print('hello ' + 'Andrei')

#print('hello ' + 5) exception

str(100)


#formatted Strings

name = 'Johnny'
age = 55 

print('Hi ' + name + '. You are ' + str(age) + ' years old')
print(f'Hi {name}. You are {age} years old')
print('Hi {}. You are {} years old'.format('Johnny','55'))
print('Hi {}. You are {} years old'.format(name,age))
print('Hi {1}. You are {0} years old'.format(age,name))


print("Hello {}, your balance is {}.".format("Cindy", 50))

print("Hello {0}, your balance is {1}.".format("Cindy", 50))

print("Hello {name}, your balance is {amount}.".format(name="Cindy", amount=50))

print("Hello {0}, your balance is {amount}.".format("Cindy", amount=50))

name = 'Cindy'
amount = 50
print(f"Hello {name}, your balance is {amount}.")