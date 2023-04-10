import random
import asyncio
from language import *

### Random name for user photo
async def random_img_name():
    name_list = list()

    for i in range(1, 15):
        name_list.append(random.randint(97, 122))

    for i in range(1, 5):
        name_list.append(random.randint(48, 57))

    name_list = [chr(i) for i in name_list]

    return "{}.jpg".format("".join(name_list))


### We clear the user text from the /get_answer command
async def clean_text(text, object):
    txt_list = [i for i in text.split(" ") if i != object]
    return " ".join(txt_list)


### Help to understand what language the user has chosen
async def lang_choose(lid, lang):
    if lid != None:
        for i in lang:
            if i in lid.lower():
                return i
            elif lid.lower()[:2] == 'ge':
                return 'deu'
            elif lid.lower()[:2] == 'fr':
                return 'fra'
    return 'eng'


### Choose language dict
async def lang_dict(user_language):
    if user_language == "English":
        return language[0]
    elif user_language == "Russian":
        return language[1]
    elif user_language == "Ukrainian":
        return language[2]
    elif user_language == "German":
        return language[3]
    elif user_language == "French":
        return language[4]



