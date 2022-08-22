
####################################
# Ex 1a

ex1_x = 5

assert ex1_x == 5

####################################
# Ex 2a

ex2_x = 3
ex2_y = 5

assert ex2_x == 3 and ex2_y == 5

####################################
# Ex 2b

ex2_z = ex2_x * ex2_y

assert ex2_z == 15

####################################
# Ex 2c

ex2_z = ex2_z - ex2_x

assert ex2_z == 12

####################################
# Ex 3a

ex3_x = 13 ** 12

assert ex3_x == 23298085122481

####################################
# Ex 3b

ex3_y = ex3_x % 17

assert ex3_y == 1

####################################
# Ex 3c

ex3_z = 3.0

assert hash(ex3_z) == 3 and type(ex3_z) is float

## OR

ex3_z = float(3)

assert hash(ex3_z) == 3 and type(ex3_z) is float

####################################
# Ex 4a

ex4_x = 'World'
ex4_y = 'Bank'

assert ex4_x == 'World' and ex4_y == 'Bank'

####################################
# Ex 4b

ex4_z = ex4_x + ' ' + ex4_y

assert ex4_z == 'World Bank'

####################################
# Ex 5a

p = 'Python'

ex5_x = p.upper()

assert ex5_x == 'PYTHON'

####################################
# Ex 5b

ex5_y = ex5_x.capitalize()

assert ex5_y == 'Python'

####################################
# Ex 6a

t = True
f = False

a = t or f

ex6_x = True

assert ex6_x == a

####################################
# Ex 6b

t = True
f = False

b = t or f
b = b and f
b = b or f
b = b and t

ex6_y = False

assert ex6_y == b

####################################
# Ex 7a

digits = [0,1,2,3,4,5,6,7,8,9] 

ex7_x = digits[0:5]

assert ex7_x == [0,1,2,3,4]

## OR

ex7_x = digits[:5]

assert ex7_x == [0,1,2,3,4]

####################################
# Ex 7b

digits = [0,1,2,3,4,5,6,7,8,9] 

ex7_y = digits[5:9]

assert ex7_y == [5,6,7,8]

####################################
# Ex 8a

digits = [[0,1,2],[3,4,5],6,[7,8,9]]

ex8_x = digits[2]

assert ex8_x == 6

####################################
# Ex 8b

digits = [[0,1,2],[3,4,5],6,[7,8,9]]

ex8_y = digits[1][1]

assert ex8_y == 4

####################################
# Ex 8c

a = 4
b = [2,3]
c = [1]

ex8_z = c
ex8_z = ex8_z + b
ex8_z.append(a)

assert ex8_z == [1,2,3,4]

####################################
# Ex 8e

a = 2
b = [1,4,3]
c = 1

ex8_k = b
ex8_k[c] = a

assert ex8_k == [1,2,3]

####################################
# Ex 8e

a = 3
b = [1,4,2]
c = 1

ex8_i = b
ex8_i.pop(c)
ex8_i.append(a)

assert ex8_i == [1,2,3]

####################################
# Ex 9a

p1 = 'pet1'
p2 = 'pet2'
Arthur = 'Cat'
b = "Dog"
c = Arthur
ex8_z = {}

ex8_z[p1] = b
ex8_z[p2] = c

assert ex8_z == {'pet1':'Dog','pet2':'Cat'}

####################################
# Ex 9b

complex_dict = {
    'alpha': [
        'a','b','c','d'
    ],
    'numbers': [
        [1,2,3],
        0,
        [-1,-2,-3]
    ],
    'symbols' : {
        'percent' : '%',
        'question' : '?',
        'tilde' : '~'
    }
}

zero = complex_dict['numbers'][1]
d = complex_dict['alpha'][3]
minus_three = complex_dict['numbers'][2][2]
symbol_list = [complex_dict['symbols']['percent'],complex_dict['symbols']['question'],complex_dict['symbols']['tilde']]

assert zero==0 and d=='d' and minus_three==-3 and symbol_list==['%','?','~']


####################################
# Ex 10a

letters = ('m','n','p')
M = letters[0]

assert type(letters) is tuple and M=='m'




