FROM python:3.11-alpine

WORKDIR /web

COPY . .
RUN pip install pipenv
RUN pipenv install --system --deploy

# RUN flask db upgrade
# RUN flask translate compile

EXPOSE 5000
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:5000", "--access-logfile", "-", "--error-logfile", "-", "app:app"]