FROM python:3.11.4-bookworm

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000



CMD ["python", "manage.py","runserver","0.0.0.0:8000"]