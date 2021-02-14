# Pull base image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/
COPY requirements.txt .
# Install dependencies

RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8000
EXPOSE 27017
