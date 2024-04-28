
# nameRoll

import datetime
import random
from data import getNameList

def take():
    name_list = getNameList()
    return random.choice(name_list)

def Roll():
    student = take()
    date = datetime.date.today()
    print(f"Date: {date}")
    print(f"the name of student is : {student}")
