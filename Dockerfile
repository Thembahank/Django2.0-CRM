FROM python:3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
# Intall dependencies
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000
ENV DOCKER_CONTAINER=1
ENV PYTHONUNBUFFERED 1



