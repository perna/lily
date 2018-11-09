FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH="$PYTHONPATH:/code"

WORKDIR /code
COPY requirements.txt ./

RUN pip install -r requirements.txt
COPY . ./

EXPOSE 8000
# TODO use gunicorn
CMD python manage.py runserver 0.0.0.0:8000
