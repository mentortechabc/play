FROM python:3.9

WORKDIR /app

# install dependencies
RUN pip install --upgrade pip
COPY src/ /app/
RUN pip install -r requirements.txt

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host", "0.0.0.0"]