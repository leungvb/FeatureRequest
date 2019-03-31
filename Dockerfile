FROM python:3.7-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY . /code

RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["sleep", "20"]
CMD ["python", "manage.py", "db", "init"]
CMD ["python", "manage.py", "db", "migrate"]
CMD ["python", "manage.py", "db", "upgrade"]

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "wsgi:app"]

#CMD ["python", "app.py"]