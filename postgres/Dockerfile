FROM python:"3.10"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /postgres
COPY requirements.txt /postgres/
RUN pip install -r requirements.txt
COPY . /postgres/
