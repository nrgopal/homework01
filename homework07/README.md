# Homework 07
This homework assignment builds on the exercises done in class in the Messaging Systems section as well as the Week 12 material for deploying a worker to k8s. At the end of those exercises, we ended up with three files, api.py, worker.py and jobs.py.

### A.
In the first in-class exercise from Week 12, we updated the Dockerfile for the flask application to include the new source code files in the Docker image and to include an entrypoint and a command that could be used for running both the flask web server and the worker.

I did the following:
- Update the code to use the IP address of the test Redis service. Be sure to 
- Built the Docker image and pushed it to the Docker Hub:
```
$ # build and push code
```
- Create a deployment for the flask API and a separate deployment for the worker:
```
$ kubectl apply -f ngopal-hw7-worker-deployment.yml
$ kubectl apply -f ngopal-hw7-flask-deployment.yml
```
- Verified that the flask API and worker are working properly: in a python debug container, create some jobs by making a POST request with curl to to flask API. Confirm that the jobs go to “complete” status by checking the Redis database in a Python shell:
```
$ #The curl statements used and the responses (output) returned by your flask APi (these should include job id’s).
$ #The Python statements (code) you issued to check the status of the jobs and the output from the statements.
```


### B.
- Update the worker deployment to pass the worker’s IP address in as an environment variable, WORKER_IP:
```
env:
  - name: WORKER_IP
    valueFrom:
      fieldRef:
        fieldPath: status.podIP
```
- Update jobs.py and/or worker.py so that when the job status is updated to in progress, the worker’s IP address is saved as new key in the job record saved in Redis. The key can be called worker and its value should be the worker’s IP address as a string:


### C.
Scale the worker deployment to 2 pods. In a python shell from within the python debug container, create 10 more jobs by making POST requests using curl to the flask API. Verify that the jobs go to “complete” status by checking the Redis database in a Python shell. Also, note which worker worked each job.

- The curl statements used and the responses (output) returned by your flask APi (these should include job id’s).

- The Python statement (code) you issued to check the status of the job and the output from the statement.

- How many jobs were worked by each worker?
