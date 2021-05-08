# FINAL
This final project works with Austin COVID-19 Complaints from the past 6 months.
The final project consists of building a REST API frontend to a time series database that allows for basic CRUD - Create, Read, Update, Delete - operations and also allows users to submit an analysis job of building a graph from the dataset.

The project includes two separate pieces of documentation: 
- DEPLOYMENT.md provides instructions for deploying the system
- DEVELOPER.md is geared towards users/developers who interact with the system


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
curl -X POST -H "content-type: application/json" -d '{"CASENUMBER": "1", "TYPEOFBUSINESS": "Bar", "TYPEOFCOMPLAINT": "Face Covering Non-Compliance", "OPENDATE": "2021-05-03", "CLOSEDATE": "2021-05-03", "OUTCOME": "No Violation(s) Found", "LATITUDE": "-88.448709", "LONGITUDE": "24.923983" }' <flask deployment pod IP>/create
```
- To delete a complaint/job entry, use the following curl statement:
```
curl <flask deployment pod IP>:5000/delete?jobid='<insert jobid>'
```
- To display all CRUD job entries, use the following curl statement:
```
curl <flask deployment pod IP>:5000/jobsubmits
```
