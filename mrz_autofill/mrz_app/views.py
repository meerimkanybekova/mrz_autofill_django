from django.shortcuts import render
from django.contrib import messages
from mrz_app.forms import PassportForm
from mrz_app.functions import *
from passporteye import read_mrz
from mrz_app.models import PassportData
from django.http import JsonResponse

def index(request):
    if request.method == 'POST':
        form = PassportForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            try:
                if chek() == 0:
                    image_file = "mrz_app/data/id.jpeg"
                    mrz = read_mrz(image_file)
                    mrz_dict = mrz.to_dict()

                    passport_data = PassportData(
                        file=request.FILES['file'],
                        name=list(mrz_dict.values())[10],
                        surname=list(mrz_dict.values())[11],
                        inn=list(mrz_dict.values())[12].replace("<", ""),
                        type_of_passport=list(mrz_dict.values())[3],
                        citizenship=get_citizenship(list(mrz_dict.values())[4]),
                        id_number=get_ID(list(mrz_dict.values())[5]),
                        data_of_birth=format_date(list(mrz_dict.values())[6]),
                        start_date=format_start_date(list(mrz_dict.values())[7]),
                        end_date=format_date(list(mrz_dict.values())[7]),
                        nationality=get_nationality(list(mrz_dict.values())[8]),
                        gender=get_gender(list(mrz_dict.values())[9])
                    )
                    passport_data.save()

                    data = {
                        'name': passport_data.name,
                        'surname': passport_data.surname,
                        'inn': passport_data.inn,
                        'type_of_passport': passport_data.type_of_passport,
                        'citizenship': passport_data.citizenship,
                        'id_number': passport_data.id_number,
                        'data_of_birth': passport_data.data_of_birth,
                        'start_date': passport_data.start_date,
                        'end_date': passport_data.end_date,
                        'nationality': passport_data.nationality,
                        'gender': passport_data.gender
                    }

                    return JsonResponse(data)
            except Exception as e:
                return JsonResponse({'error': 'Загрузите фото получше для лучшей точности.'}, status=400)
    elif request.method == 'GET':
        form = PassportForm()
        return render(request, 'index.html', {'form': form})

    return JsonResponse({'error': 'Invalid request method'}, status=405)


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
