FROM python:3.10
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt

RUN apt-get update 
RUN apt-get install -y ffmpeg
RUN pip install -r requirements.txt

COPY . /app
CMD ["python", "web_app.py"]