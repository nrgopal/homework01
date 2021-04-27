FROM python:3.9
ENV LC_CTYPE=en.US.UTF-8
ENV LANG=en_US.UTF-8
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY source /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
