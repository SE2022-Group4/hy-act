FROM python:3.8

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY .. .

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "hy_act_server.wsgi:application"]