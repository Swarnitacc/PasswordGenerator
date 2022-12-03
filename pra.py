#project 1 :- Create a code generator. This can that take text as input, replaces each letter with another letter, 
# and outputs the “encoded” message.

'''For this challenge, we will use a Python script to
 generate a random password of 8 characters. Each time 
 the program is run, a new password will be generated randomly.
  The passwords generated will be 8 characters long and will have 
  to include the following characters in any order:
2 uppercase letters from A to Z,
2 lowercase letters from a to z,
2 digits from 0 to 9,
2 punctuation signs such as !, ?, “, # etc.'''

'''Second Commit'''



# import random
# password = random.randint(64-91)

import string
import random
 
# Randomly choose a letter from all the ascii_letters

def pst():
    randomLetter = chr(random.randint(ord('a'),ord('z')))
    randomcapLetter = chr(random.randint(ord('A'),ord('B')))
    random_number =  random.randint(1,100)
    randomchrs = chr(random.randint ((33),(38)))
    Password =(f'{randomLetter}{randomcapLetter}{random_number}{randomLetter}{randomcapLetter}{random_number}{randomchrs}{randomchrs}')
    # print(Password)
    s = ''.join(random.sample(Password,len(Password)))
    return(s)

#how to shuffle these numbers ? can F string be used in shuffle method
# print(__doc__)

print(pst())

# from xmlrpc.server import DocCGIXMLRPCRequestHandler


# def format_name():
#     f = input("Enter a name")
#     l = input("Enter last name")
#     f_name = (f.capitalize())
#     l_name = (l.capitalize())
#     print (f"{f_name} {l_name}")

# format_name()








  

