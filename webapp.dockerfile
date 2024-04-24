FROM python:3.10

RUN apt-get update \
	&& apt-get install -y --no-install-recommends
	
WORKDIR /app
COPY webapp/ /app/
RUN pip3 install -r requirements.txt

EXPOSE 3000