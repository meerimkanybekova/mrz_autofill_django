import datetime

def handle_uploaded_file(f):
    with open("mrz_app/data/id.jpeg", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def get_citizenship(kgz):
    if kgz == "KGZ":
        return "Кыргызская Республика"
    else:
        return "unknown"

def get_nationality(nation):
    if nation == "KGZ":
        return "кыргыз/ка"

def get_gender(gender):
    if gender == "F":
        return "Женский"
    elif gender == "M":
        return "Мужской"
    else:
        return "invalid"

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

    return f"{year}.{month}.{int(day)-10}"