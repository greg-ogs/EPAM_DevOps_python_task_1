FROM python:3.14.0a2-bullseye
LABEL authors="grego"

ENTRYPOINT ["/bin/bash"]

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt
