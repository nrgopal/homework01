# Homework 06
In this homework we are deploying our Flask API to k8s. Our goal today is to create a “test” environment for our Flask API application.
In each step I created a k8s object described in a separate yml file.

## Step 1: Create a persistent volume claim for your Redis data.
I did the following when writing the PVC:
- Added a username label and an env label. The value for username is my tacc username and the value for env should be test, to indicate that this is the test environment.
- The accessModes should include a single entry, readWriteOnce.
- The storageClassName should be rbd.
- Request 1 GB (1Gi) of storage.

To create the redis PVC:
```
$ kubectl apply -f ngopal-test-redis-pvc.yml
```

### Step 2: Create a deployment for the Redis database.
I did the following when writing the deployment: 
- Added the same username and env labels for both the deployment and the pod template.
- Set replicas: 1 as Redis is a stateful application.
- For the image, I used redis:5.0.0; did not set a command.
- Added the username and env lables to the pod as well.
- Added an app label with value ngopal-test-redis.
- Defined volumeMount and associate it with a volume that is filled by the PVC created in Step 1. For the mount path, use /data, as this is where Redis writes its data.

To create the redis deployment:
```
$ kubectl apply -f ngopal-test-redis-deployment.yml
```

### Step 3: Create a service for the Redis database.
I did the following when writing the service: 
- Added the same username and env labels for both the deployment and the pod template.
- Made the type of service ClusterIP.
- Defined a selector that will elect only these Redis pods.
- Added port and targetPort that match the Redis port.

To create the redis service:
```
$ kubectl apply -f ngopal-test-redis-service.yml
```

### Step 4: Create a deployment for the flask API.
I did the following when writing the deployment: 
- Added the same username and env labels for both the deployment and the pod template.
- Start 2 replicas of your flask API pod.
- Expose port 5000.

To create the flask deployment:
```
$ kubectl apply -f ngopal-test-flask-deployment.yml
```

### Step 5: Create a service for the flask API, with a persistent IP address to use to talk to the flask API, regardless of the IPs that may be assigned to individual flask API pods.
I did the following when writing the service: 
- Added the same username and env labels for both the deployment and the pod template.
- Made the type of service ClusterIP.
- Defined a selector that will select only these flask API pods.
- Added port and targetPort that match the flask port.

To create the redis service:
```
$ kubectl apply -f ngopal-test-flask-service.yml
```

### Check the work done in Steps 1-3.
Create a “debug” deployment:
```
$ kubectl apply -f deployment-python-debug.yml
```

Look up the service IP address for the test redis service:
```
$ kubectl get services
```

Look up the service IP address for the test redis service:
```
$ kubectl get services
```

Determine the pod name of the python debug deployment:
```
$ kubectl get pods
```

Exec into a Python debug container:
```
$ kubectl exec -it py-debug-deployment-<##########>-<#####> -- /bin/bash
```

Install the redis python library:
```
$ pip3 install --user redis
```

Launch the python shell:
```
$ python3
```

Import redis:
```
>>> import redis
```

Create a Python redis client object using the IP and port of the service:
```
>>> rd = redis.StrictRedis(host='##.###.###.###', port=6379, db=0)
```

Create a key and make sure you can get the key:
```
>>> rd.set('name', '<insert name>')
```

In another shell on isp02, delete the redis pod. Check that k8s creates a new redis pod:
```
$ kubectl delete pods ngopal-test-redis-deployment-#########-#####
$ kubectl get pods
```

Back in your python shell, check that you can still get the key using the same IP:
```
>>> rd.get('name')
```
This will show that your service is working and that your Redis database is persisting data to the PVC (i.e., the data are surviving pod restarts).

### Updating the Flask API to use the Redis Service IP
In our app.py we need to pass the Redis IP as an environment variable to our service. Environment variables are variables that get set in the shell and are available for programs. In python, the os.environ dictionary contains a key for every variable.

Add the following to the app.py:
```
import os

redis_ip = os.environ.get('REDIS_IP')
if not redis_ip:
    raise Exception()
rd=redis.StrictRedis(host=redis_ip, port=6379, db=0)
```
This way, if we set an environment variable called REDIS_IP to our Redis service IP before starting our API, the flask code will automatically pick it up and use it.
