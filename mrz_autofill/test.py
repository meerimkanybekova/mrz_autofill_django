from passporteye import read_mrz
import re

image_file = "mrz_app/data/id.jpeg"
mrz = read_mrz(image_file)
mrz_dict = mrz.to_dict()
pic_again = 45

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
  
import datetime
def format_date(birthday):
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


    day = int(day)
    if day >= 30:
        day = 1900 + day
    else:
        day = 2000 + day

    return f"{year}.{month}.{day}"

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

    return f"{year}.{month}.{2000 + int(day)-10}"

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
