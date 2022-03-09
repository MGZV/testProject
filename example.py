import random
import pandas as pd

# Inputs
letters = "АБВГДЕЖИКЛМНОПРСТУФХЦЧШЭЮЯ"
numbers = "123456789"
cod_list = []
count = 0
cod_count = int(input("Enter cod count:"))

# Code work
def generate_cod():
    letters_cod = ""
    numbers_cod = ""
    for i in range(0, 3):
        letters_cod += random.choice(letters)

    for i in range(0, 8):
        numbers_cod += random.choice(numbers)
        if len(numbers_cod) == 3:
            numbers_cod += "."
        if len(numbers_cod) == 6:
            numbers_cod += "."
    return letters_cod + " " + numbers_cod


while count != cod_count:
    cod_list.append(generate_cod())
    count += 1

# Result
cod_dict = {"Код": cod_list}

ordered_cod_dict = pd.DataFrame(cod_dict)
ordered_cod_dict.index += 1
ordered_cod_dict.to_excel("file_name.xlsx")