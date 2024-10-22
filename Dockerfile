FROM python:3.10

WORKDIR /code

COPY requirements.txt /code/

RUN python -m pip install --upgrade pip 
RUN python -m pip install -r requirements.txt 

COPY . /code/

EXPOSE 8000

# Comando para iniciar la aplicación
CMD ["gunicorn", "django_prueba_app.wsgi:application", "--bind", "0.0.0.0:8000"]