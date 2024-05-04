FROM python:3.12-alpine

RUN adduser -D bio-quiz

WORKDIR /home/bio-quiz

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY bio-quiz.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP bio-quiz.py

RUN chown -R bio-quiz:bio-quiz ./
USER bio-quiz

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]