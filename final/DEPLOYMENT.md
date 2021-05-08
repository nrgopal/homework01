### DEPLOYMENT 
- Build the Docker image and push it to the Docker Hub using the Makefile:
```
$ make build-final
```
- Create deployments for the flask API, flask service, and the worker:
```
$ kubectl apply -f ngopal-final-flask-deployment.yml
$ kubectl apply -f ngopal-final-flask-service.yml
$ kubectl apply -f ngopal-final-worker-deployment.yml
```
