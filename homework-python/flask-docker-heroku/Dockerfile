FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python3-pip build-essential
COPY src /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD ["python3", "app.py"]