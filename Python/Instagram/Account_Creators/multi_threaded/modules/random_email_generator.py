
"""
    author: Sylar
    RANDOM email generator
"""
from string import digits
from string import ascii_letters as letters
from random import choice, randint
from modules.config import MODULES_DIR


def tld():
	filepath = '/tdls.txt'
	with open(MODULES_DIR + filepath,'r') as reader:
		f = reader.readlines()
		r = choice(f)
		return r

sizer = randint(5,9)
		
def first(evt = None, size=sizer, chars = letters):
	id = ''.join(choice(chars) for _ in range(size))
	return id
	
sizer2 = randint(5,9)
	
def second(evt = None, size=sizer2, chars = letters):
	id = ''.join(choice(chars) for _ in range(size))
	return id
	
sizer3 = randint(8, 12)
	
def passwd(evt = None, size=sizer3, chars = letters + digits):
	id = ''.join(choice(chars) for _ in range(size))
	return id
	
def random_email_generator():
	new_string = str( first() + "@" + second() + "." + tld().lower() )
	return new_string
	
if __name__ == "__main__":
	random_email_generator()
