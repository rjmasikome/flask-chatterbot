FROM python:2

ADD app.py /

RUN pip install flask
RUN pip install chatterbot
RUN pip install sqlalchemy

CMD [ "python", "./app.py" ]