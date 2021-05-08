### DEVELOPER
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