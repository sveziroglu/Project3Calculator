FROM python:3.7-alpine

WORKDIR /flaskproject

ADD . /flaskproject

RUN pip install -r requirements.txt

CMD ["python", "app.py"]


