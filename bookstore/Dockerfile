FROM python:"3.10"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /bookstore

COPY requirements.txt /bookstore/
RUN pip install -r requirements.txt
COPY . /bookstore/
