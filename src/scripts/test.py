from os import listdir
from random import choice
text_style = f"text_styles/{choice(listdir('text_styles'))}"

with open(text_style, "r") as f:
    print(text_style)
    print(f.read())