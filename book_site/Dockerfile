FROM python:3.8

WORKDIR usr/src/book_site


ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
    && apt-get install netcat -y

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .


RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]

