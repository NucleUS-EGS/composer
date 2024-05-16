FROM python:3.10

RUN apt-get update \
	&& apt-get install -y --no-install-recommends
	
WORKDIR /app

COPY webapp/requirements.txt /app/
RUN pip3 install -r requirements.txt

COPY webapp/ /app/

EXPOSE 3000

CMD ["sh", "-c", "python3 manage.py migrate --noinput && python3 manage.py runserver 0.0.0.0:3000 --noreload"]