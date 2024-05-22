# Base image
FROM python:3.10

RUN apt-get update \
	&& apt-get install -y --no-install-recommends

WORKDIR /app

COPY points/requirements.txt /app/
RUN pip3 install -r requirements.txt

COPY points/ /app/

# CMD ["python", "app.py"]
CMD ["flask", "run"]