FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY . /code

RUN pip install --trusted-host pypi.python.org -r requirements.txt


#CMD ["python", "app.py"]