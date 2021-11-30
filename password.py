#Python Random Password Generator 

LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = "abcdefghijklmnopqrstuvwxyz"
NUMBERS = "0123456789"
SYMBOLS = "[]}{()*;/,_-"

all = LOWER + UPPER + NUMBERS + SYMBOLS

Length = 16

Password = " " .join(random.sample(all.length))

print(Password)
