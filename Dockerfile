FROM python:3.7.3-slim

ARG MODEL="en_core_web_sm"

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

RUN python -m spacy download ${MODEL}

COPY . /app 

EXPOSE 8000

CMD uvicorn main:app --host 0.0.0.0 --port 8000