FROM ubuntu:latest
ENV LC_CTYPE=en.US.UTF-8
ENV LANG=en_US.UTF-8
RUN apt-get update -y
RUN apt-get install -y python3-dev python3-pip3 build-essential
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]
