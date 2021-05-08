# FINAL
This final project works with real Austin COVID-19 Complaints from the past 6 months.

### A. 
- Built the Docker image and pushed it to the Docker Hub:

```
$ make build-final
```
- Create a deployment for the flask API and a separate deployment for the worker:
```
$ kubectl apply -f ngopal-hw7-worker-deployment.yml
$ kubectl apply -f ngopal-hw7-flask-deployment.yml
```
- Verified that the flask API and worker are working properly: in a python debug container, create some jobs by making a POST request with curl to to flask API. Confirm that the jobs go to “complete” status by checking the Redis database in a Python shell:
```
$ curl -X POST -H "content-type: application/json" -d '{"start": "START", "end":"END"}' 10.107.124.53:5000/jobs
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
```
if(new_status == 'in progress'):
        worker_IP = os.environ.get('WORKER_IP')
        print(worker_IP)
        rd.hset(_generate_job_key(jid), 'worker', worker_IP)
```

### C.
- Scale the worker deployment to 2 pods. In a python shell from within the python debug container, create 10 more jobs by making POST requests using curl to the flask API. Verify that the jobs go to “complete” status by checking the Redis database in a Python shell. Also, note which worker worked each job.
```
$ curl -X POST -H "content-type: application/json" -d '{"start": "START", "end":"END"}' 10.107.124.53:5000/jobs
```

- The Python statement (code) you issued to check the status of the job and the output from the statement:
```
>>>   print(key)
>>>   rd.hget(key, 'worker')
```

