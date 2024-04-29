# Base image
FROM python:3.10

RUN apt-get update \
	&& apt-get install -y --no-install-recommends

# Execute the command to create a folder
RUN mkdir /app

# Define the working directory of a Docker container
WORKDIR /app

# Copy external files into the working directory
COPY points-system/requirements.txt /app/

# Execute the pip to install the dependencies
RUN pip install -r requirements.txt

# Copy the external code into the working directory
COPY points-system/ /app/