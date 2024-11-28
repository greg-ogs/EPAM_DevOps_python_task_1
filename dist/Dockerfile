FROM python:3.14.0a2-bullseye
LABEL authors="grego"

ENTRYPOINT ["/bin/bash"]

WORKDIR /app

COPY pytask-0.1.0-py3-none-any.whl .

RUN pip install pytask-0.1.0-py3-none-any.whl