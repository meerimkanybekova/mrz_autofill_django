from django.db import models

class PassportData(models.Model):
	file = models.FileField(upload_to='uploads/')

	name = models.CharField(max_length=255)
	surname = models.CharField(max_length=255)
	citizenship = models.CharField(max_length=255)
	nationality = models.CharField(max_length=255)
	id_number = models.CharField(max_length=255)
	gender = models.CharField(max_length=255)
	type_of_passport = models.CharField(max_length=255)

	inn = models.BigIntegerField(max_length=255)

	data_of_birth = models.DateField(max_length=255)
	start_date = models.DateField(max_length=255)
	end_date = models.DateField(max_length=255)

	def __str__(self):
		return f"{self.name} {self.surname}"
