# FINAL
This final project works with Austin COVID-19 Complaints from the past 6 months.

### A. 
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
- Copy the flask deployment pod name and IP address for the next steps.
```
$ kubectl get pods -o wide
```
- Exec into the flask deployment pod to curl the CRUD routes and test the functionality of the system:
```
$ kubectl exec -it ngopal-final-flask-deployment-<insert flask deployment pod name> -- /bin/bash
```
- To create a complaint/job entry, use the following curl statement:
```
curl -X POST -H "content-type: application/json" -d '{"CASENUMBER": "1", "TYPEOFBUSINESS": "Bar", "TYPEOFCOMPLAINT": "Face Covering Non-Compliance - Business", "OPENDATE": "2021-05-03", "CLOSEDATE": "2021-05-03", "OUTCOME": "No Violation(s) Found/Inspection Performed", "LATITUDE": "-88.448709", "LONGITUDE": "24.923983" }' <flask deployment pod IP>:5000/create
```
- To delete a complaint/job entry, use the following curl statement:
```
curl <flask deployment pod IP>:5000/delete?jobid='<insert jobid>'
```
- To display all CRUD job entries, use the following curl statement:
```
curl <flask deployment pod IP>:5000/jobsubmits
```
