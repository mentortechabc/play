FROM python:3.9

WORKDIR /app

# install dependencies
RUN pip install --upgrade pip
COPY src/ /app/
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]