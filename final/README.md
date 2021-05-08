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
- Exec into the flask deployment pod to curl the CRUD routes and test the functionality of the system:
```
$ kubectl exec -it nrgopal-final-flask-deployment-### -- /bin/bash
```
- To create a complaint/job entry, use the following curl statement:
```
curl -X POST -H "content-type: application/json" -d '{"CASENUMBER": "1-demo", "TYPEOFBUSINESS": "Bar", "TYPEOFCOMPLAINT": "Face Covering Non-Compliance - Business", "OPENDATE": "2021-05-07", "CLOSEDATE": "2021-05-07", "OUTCOME": "No Violation(s) Found/Inspection Performed", "ADDRESS": "13435 N 183 HWY NB", "LATITUDE": "-88.448709", "LONGITUDE": "24.923983" }' ###:5000/create
```
- To delete a complaint/job entry, use the following curl statement:
```
curl ###:5000/delete?jobid='######'
```
- To display all CRUD job entries, use the following curl statement:
```
curl ###:5000/jobsubmits'
```
