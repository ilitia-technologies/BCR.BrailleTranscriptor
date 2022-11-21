FROM python:3.9

RUN apt-get update
#RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . /app

EXPOSE 8001

WORKDIR /app
ENTRYPOINT ["python", "app.py"]

