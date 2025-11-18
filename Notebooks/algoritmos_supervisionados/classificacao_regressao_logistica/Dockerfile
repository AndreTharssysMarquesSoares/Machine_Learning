FROM python:3.12 

WORKDIR /code/app

# pip freeze > requirements.txt
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

# docker build -t modeloqualidadefrutas .
# docker run -d --name mymodelapp -p 80:80 modeloqualidadefrutas