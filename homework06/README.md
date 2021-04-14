# Homework 06

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
