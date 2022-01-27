FROM python:3.10-alpine

RUN pip install fastapi

RUN pip install uvicorn

RUN pip install pymongo

RUN pip install requests

COPY . .

CMD python3 modele_personne.py
