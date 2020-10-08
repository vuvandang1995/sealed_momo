FROM python:3.6 as app
WORKDIR /app
COPY requirements.txt /app
RUN  pip install -r requirements.txt
RUN apt-get update && apt-get install -y wget && wget https://github.com/bitnami-labs/sealed-secrets/releases/download/v0.12.1/kubeseal-linux-amd64 -O kubeseal && install -m 755 kubeseal /usr/local/bin/kubeseal
COPY . /app
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "sealed_momo.wsgi"]

FROM nginx as webapp
WORKDIR /static
ADD ./client/static /static
EXPOSE 80