# Homework 06

## Step 1:

'''

hi

'''


Some basic Git commands are:
```
git status
git add
git commit
```

### read_animals.py
Pick two random animals and ‘breed’ them by adding their elements to create a new offspring, which is printed to screen along with its ‘parents’

### test_read_animals.py
Unit test that checks for the new functionality in read_animals.py and is executable from the command line.
Makes sure that the characteristics of the offspring match those of its parents.

## Installation

### Install this project by cloning the repository, making the scripts executable, and adding them to your PATH: 

git clone https://github.com/nrgopal/nrgopal-coe332/homework02

touch Dockerfile


### Assemble Dockerfile by adding the following:
FROM centos:7.7.1908

RUN yum update -y && yum install -y python3

ENV LC_CTYPE=en_US.UTF-8
ENV LANG=en_US.UTF-8

RUN pip3 install petname==2.6

COPY generate_animals.py /code/generate_animals.py
COPY read_animals.py /code/read_animals.py

RUN chmod +rx /code/generate_animals.py && \
    chmod +rx /code/read_animals.py

ENV PATH "/code:$PATH"

### Update and upgrade and install required packages:
docker run --rm -it -v $PWD:/code centos:7.7.1908 /bin/bash

yum update

yum install python3
python3 --version
pip3 install petname==2.6

export LC_CTYPE=en_US.UTF-8
export LANG=en_US.UTF-8
pip3 install petname

cd /code
chmod +rx generate_animals.py
chmod +rx read_animals.py
chmod +rx test_read_animals.py
export PATH=/code:$PATH

## Docker Image

### You can build a Docker image using the provided Dockerfile. Use the commands:
docker build -t username/json-parser:1.0 .


## Test

### Test examples of executing the scripts inside a container by running:
docker run --rm -it username/json-parser:1.0 /bin/bash
cd /home
generate_animals.py test.json
ls
read_animals.py test.json
ls

### Next, exit the container and test the code non-interactively:
docker run --rm -v $PWD:/data username/json-parser:1.0 generate_animals.py /data/animals.json
ls -l

## We can test the newly-built image interactively, we will use docker run to start a shell inside the image:

rm animals.json
docker run --rm -v $PWD:/data -u $(id -u):$(id -g) username/json-parser:1.0 generate_animals.py /data/animals.json
ls -l

docker run --rm -v $PWD:/data username/json-parser:1.0 read_animals.py /data/animals.json
