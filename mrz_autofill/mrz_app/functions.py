import datetime

def handle_uploaded_file(f):
    with open("mrz_app/data/id.jpeg", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def format_date(birthday):
    if len(birthday) == 6:
        day = birthday[0:2]
        month = birthday[2:4]
        year = birthday[4:6]

        day = int(day)
        if day >= 30:
            day = 1900 + day
        else:
            day = 2000 + day
    else:
        day = birthday[4:6]
        month = birthday[2:4]
        year = birthday[0:2]

        current_year = datetime.datetime.now().year
        century = current_year // 100
        year = str(century * 100 + int(year))

        day = int(day)
        if day >= 30:
            day = 1900 + day
        else:
            day = 2000 + day

    return f"{day}-{month}-{year}"

def format_start_date(birthday):
    if len(birthday) == 6:
        day = birthday[0:2]
        month = birthday[2:4]
        year = birthday[4:6]
    else:
        day = birthday[4:6]
        month = birthday[2:4]
        year = birthday[0:2]

        current_year = datetime.datetime.now().year
        century = current_year // 100
        year = str(century * 100 + int(year))

    return f"{2000+int(day)-10}-{month}-{year}"

def get_ID(id):
    if id.startswith("1"):
        id = "I" + id[1:]

    return id

import re

pic_again = "  "

def get_citizenship(kgz):
  if kgz == "KGZ":
    return "Кыргызская Республика"
  else:
    return pic_again

def get_nationality(nation):
  if nation == "KGZ":
    return "кыргыз/ка"
  else:
    return pic_again
  
def get_gender(gender):
  if gender == "F":
    return "Женский"
  elif gender == "M":
    return "Мужской"
  else:
    return pic_again
  

def check_letters(string):
    if re.match(r'^[a-zA-Z]+$', string):
        return string
    else:
        return pic_again

def check_not_letters(string):
    if any(char.isalpha() for char in string):
        return pic_again
    else:
        return string
    
def check_type_of_pasport(string):
    if string == "ID" or string == "AN":
        return string
    else:
        return pic_again
    
def check_pasport(string):
    if string[:2] == "ID" or string[:2] == "AN":
        return string
    else:
        return pic_again

def check(string):
    if "<" in string:
        pic_again
    else:
        return string

def check_ints_inn(string):
  int_count = 0
  for char in string:
      if char.isdigit():
          int_count += 1

  if int_count == 14:
      return string
  else:
      return pic_again

from passporteye import read_mrz

image_file = "mrz_app/data/id.jpeg"
mrz = read_mrz(image_file)
mrz_dict = mrz.to_dict()

def chek():
    fail = 0
    try:
        name = list(mrz_dict.values())[10].replace("<", "")
        surname = list(mrz_dict.values())[11].replace("<", "")
        inn = check_ints_inn(list(mrz_dict.values())[12].replace("<", ""))
        type_of_passport = (list(mrz_dict.values())[3].replace("<", ""))
        citizenship = get_citizenship(list(mrz_dict.values())[4]).replace("<", "")
        passport_id = (list(mrz_dict.values())[5].replace("<", ""))
        date_of_birth = format_date(list(mrz_dict.values())[6])
        start_date = check_not_letters(format_start_date(list(mrz_dict.values())[7]))
        finish_date = check_not_letters(format_date(list(mrz_dict.values())[7]))
        nationality = get_nationality(list(mrz_dict.values())[8])
        gender = get_gender(list(mrz_dict.values())[9]).replace("<", "")
        
        # print("All operations executed successfully.")

        mylist = (name, surname, inn, type_of_passport, date_of_birth, citizenship, passport_id, start_date, finish_date, nationality, gender)

        for d in mylist:
            br = False
            if d == pic_again:
                fail = 1
                br = True

            if br == False:
                fail = 0

    except Exception as e:
        fail = 1

    return fail
