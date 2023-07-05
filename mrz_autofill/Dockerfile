FROM python:3.10

WORKDIR /mrz_autofill

COPY . /mrz_autofill/

RUN pip install -r requirements.txt

WORKDIR /mrz_autofill/mrz_app

EXPOSE 8000

CMD python ../manage.py runserver 0.0.0.0:8000
