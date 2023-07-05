from rest_framework import serializers
from .models import PassportData

class PassportDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassportData
        fields = ['file', 'name', 'surname', 'citizenship', 'nationality', 'id_number', 'gender', 'type_of_passport', 'inn', 'data_of_birth', 'start_date', 'end_date']