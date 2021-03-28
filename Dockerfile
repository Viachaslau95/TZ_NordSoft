
# pull official base image
FROM python:3.8

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/TZ_NordSoft


# install dependencies
COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt

# copy project
COPY . /usr/src/TZ_NordSoft

EXPOSE 8000/tsp


