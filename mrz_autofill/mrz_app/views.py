from django.shortcuts import render, redirect
from django.contrib import messages
from mrz_app.forms import PassportForm
from mrz_app.functions import handle_uploaded_file, get_citizenship, get_nationality, get_gender, format_date, format_start_date
from passporteye import read_mrz
from mrz_app.models import PassportData

type_of_passport = 3
citizenship = 4
id_number = 5
data_of_birth = 6
expiration_date = 7
nationality = 8
gender = 9
name = 10
surname = 11
inn = 12

def index(request):
    if request.method == 'POST':
        form = PassportForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            image_file = "mrz_app/data/id.jpeg"
            mrz = read_mrz(image_file)
            mrz_dict = mrz.to_dict()

            passport_data = PassportData(
                file=request.FILES['file'],
                name=list(mrz_dict.values())[name],
                surname=list(mrz_dict.values())[surname],
                inn=list(mrz_dict.values())[inn].replace("<", ""),
                type_of_passport=list(mrz_dict.values())[type_of_passport],
                citizenship=get_citizenship(list(mrz_dict.values())[citizenship]),
                id_number=list(mrz_dict.values())[id_number],
                data_of_birth=format_date(list(mrz_dict.values())[data_of_birth]),
                start_date=format_start_date(list(mrz_dict.values())[expiration_date]),
                end_date=format_date(list(mrz_dict.values())[expiration_date]),
                nationality=get_nationality(list(mrz_dict.values())[nationality]),
                gender=get_gender(list(mrz_dict.values())[gender])
            )
            passport_data.save()

            context = {
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

            messages.success(request, "Данные сохранены")
            return render(request, 'index.html', context)
    else:
        form = PassportForm()

    return render(request, "index.html", {'form': form})
