import string
import random


def genPwd(length, upper='', lower='', nums='', specials=''):
  #including the possible characters
  char_upper = string.ascii_uppercase
  char_lower = string.ascii_lowercase
  char_num   = string.digits
  char_special = string.punctuation

  chars = [];

  chars.extend(char_upper)
  chars.extend(char_lower)
  chars.extend(char_num)
  #chars.extend(char_special)

  if not chars:
    print("ERROR: chars is empty")
    return None

  pwd = "";

  for char in range(length):
    #print(f'pwd: {pwd}')
    pwd += random.choice(chars)

  return pwd


print(genPwd(40))