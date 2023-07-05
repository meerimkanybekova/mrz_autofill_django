from rest_framework.views import APIView
from rest_framework.response import Response
from passporteye import read_mrz
import datetime
import re

class PassportAPIView(APIView):
    def post(self, request):
        try:
            image_file = request.FILES.get('image_file')
            mrz = read_mrz(image_file)
            mrz_dict = mrz.to_dict()
            
            pic_again = "Данные плохо видны. Пожалуйста, сделайте фото еще раз качественнее."

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

            def check_type_of_passport(string):
                if string == "ID" or string == "AN":
                    return string
                else:
                    return pic_again

            def check_passport(string):
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

            def pic():
                return pic_again

            name = list(mrz_dict.values())[10].replace("<", "")
            surname = list(mrz_dict.values())[11].replace("<", "")
            inn = check_ints_inn(list(mrz_dict.values())[12].replace("<", ""))
            type_of_passport = (list(mrz_dict.values())[3].replace("<", ""))
            citizenship = get_citizenship(list(mrz_dict.values())[4]).replace("<", "")
            passport_id = (list(mrz_dict.values())[5].replace("<", ""))
            start_date = check_not_letters(format_start_date(list(mrz_dict.values())[7]))
            finish_date = check_not_letters(format_date(list(mrz_dict.values())[7]))
            nationality = get_nationality(list(mrz_dict.values())[8])
            gender = get_gender(list(mrz_dict.values())[9]).replace("<", "")

            data = {
                "name": name,
                "surname": surname,
                "inn": inn,
                "type_of_passport": type_of_passport,
                "citizenship": citizenship,
                "passport_id": passport_id,
                "start_date": start_date,
                "finish_date": finish_date,
                "nationality": nationality,
                "gender": gender
            }

            return Response(data)
        except Exception as e:
            return Response({"error": str(e)})


# from django.shortcuts import render
# from django.contrib import messages
# from mrz_app.forms import PassportForm
# from mrz_app.functions import *
# from passporteye import read_mrz
# from mrz_app.models import PassportData
# from django.http import JsonResponse

# def index(request):
#     if request.method == 'POST':
#         form = PassportForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             try:
#                 if chek() == 0:
#                     image_file = "mrz_app/data/id.jpeg"
#                     mrz = read_mrz(image_file)
#                     mrz_dict = mrz.to_dict()

#                     passport_data = PassportData(
#                         file=request.FILES['file'],
#                         name=list(mrz_dict.values())[10],
#                         surname=list(mrz_dict.values())[11],
#                         inn=list(mrz_dict.values())[12].replace("<", ""),
#                         type_of_passport=list(mrz_dict.values())[3],
#                         citizenship=get_citizenship(list(mrz_dict.values())[4]),
#                         id_number=get_ID(list(mrz_dict.values())[5]),
#                         data_of_birth=format_date(list(mrz_dict.values())[6]),
#                         start_date=format_start_date(list(mrz_dict.values())[7]),
#                         end_date=format_date(list(mrz_dict.values())[7]),
#                         nationality=get_nationality(list(mrz_dict.values())[8]),
#                         gender=get_gender(list(mrz_dict.values())[9])
#                     )
#                     passport_data.save()

#                     data = {
#                         'name': passport_data.name,
#                         'surname': passport_data.surname,
#                         'inn': passport_data.inn,
#                         'type_of_passport': passport_data.type_of_passport,
#                         'citizenship': passport_data.citizenship,
#                         'id_number': passport_data.id_number,
#                         'data_of_birth': passport_data.data_of_birth,
#                         'start_date': passport_data.start_date,
#                         'end_date': passport_data.end_date,
#                         'nationality': passport_data.nationality,
#                         'gender': passport_data.gender
#                     }

#                     return JsonResponse(data)
#             except Exception as e:
#                 return JsonResponse({'error': 'Загрузите фото получше для лучшей точности.'}, status=400)
#     elif request.method == 'GET':
#         form = PassportForm()
#         return render(request, 'index.html', {'form': form})

#     return JsonResponse({'error': 'Invalid request method'}, status=405)

# from django.shortcuts import render
# from django.contrib import messages
# from mrz_app.forms import PassportForm
# from mrz_app.functions import *
# from passporteye import read_mrz
# from mrz_app.models import PassportData

# def index(request):
#     if request.method == 'POST':
#         form = PassportForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             try:
#                 if chek() == 0:
#                     image_file = "mrz_app/data/id.jpeg"
#                     mrz = read_mrz(image_file)
#                     mrz_dict = mrz.to_dict()

#                     passport_data = PassportData(
#                         file=request.FILES['file'],
#                         name=list(mrz_dict.values())[10],
#                         surname=list(mrz_dict.values())[11],
#                         inn=list(mrz_dict.values())[12].replace("<", ""),
#                         type_of_passport=list(mrz_dict.values())[3],
#                         citizenship=get_citizenship(list(mrz_dict.values())[4]),
#                         id_number=get_ID(list(mrz_dict.values())[5]),
#                         data_of_birth=format_date(list(mrz_dict.values())[6]),
#                         start_date=format_start_date(list(mrz_dict.values())[7]),
#                         end_date=format_date(list(mrz_dict.values())[7]),
#                         nationality=get_nationality(list(mrz_dict.values())[8]),
#                         gender=get_gender(list(mrz_dict.values())[9])
#                     )
#                     passport_data.save()

#                     context = {
#                         'name': passport_data.name,
#                         'surname': passport_data.surname,
#                         'inn': passport_data.inn,
#                         'type_of_passport': passport_data.type_of_passport,
#                         'citizenship': passport_data.citizenship,
#                         'id_number': passport_data.id_number,
#                         'data_of_birth': passport_data.data_of_birth,
#                         'start_date': passport_data.start_date,
#                         'end_date': passport_data.end_date,
#                         'nationality': passport_data.nationality,
#                         'gender': passport_data.gender
#                     }

#                     messages.success(request, "Данные сохранены")
#                     return render(request, 'index.html', context)
#             except Exception as e:
#                 messages.success(request, "Загрузите фото получше для лучшей точности.")
#                 return render(request, 'index.html')
#     else:
#         form = PassportForm()

#     return render(request, "index.html", {'form': form})
