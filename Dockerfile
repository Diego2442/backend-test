FROM python:3.10

WORKDIR /code

COPY requirements.txt /code/

RUN python -m pip install --upgrade pip 
RUN python -m pip install -r requirements.txt 

COPY . /code/

EXPOSE 8000