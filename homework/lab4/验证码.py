

import random
import string

def captcha(n):
    captcha_4 = ''
    character = string.digits + string.ascii_uppercase
    for count in range(0,4):
        char = random.choice(character)
        captcha_4 += char
    print(captcha_4)

captcha(4)