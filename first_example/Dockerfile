FROM python: "3.10"

ENV PYTHONDONTWRITEBYTECODE = 1
ENV PYTHONUNBUFFERED = 1

WORKDIR /first_example

COPY requirements.txt /first_example/

RUN pip install -r requirements.txt
COPY . /first_example/
