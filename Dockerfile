FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH="$PYTHONPATH:/code"

WORKDIR /code
COPY requirements.txt ./

RUN pip install -r requirements.txt
COPY . ./

EXPOSE 8000
CMD gunicorn -w 4 -b :8000 lily.wsgi
