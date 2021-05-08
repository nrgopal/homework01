### DEVELOPER
- Copy the flask deployment pod name and IP address for the next steps.
```
$ kubectl get pods -o wide
```
```
NAME                                             READY   STATUS    RESTARTS   AGE   IP              NODE                         NOMINATED NODE   READINESS GATES
ngopal-final-flask-deployment-7dd864b899-5rrct   1/1     Running   0          23s   10.244.13.216   c11                          <none>           <none>
ngopal-final-worker-deployment-dfc889c7-qns4h    1/1     Running   0          4s    10.244.13.218   c11                          <none>           <none>
py-debug-deployment-5cc8cdd65f-s95zk             1/1     Running   0          28h   10.244.10.92    c009.rodeo.tacc.utexas.edu   <none>           <none>
redis-pvc-deployment-final-6764d747df-vthl9      1/1     Running   0          28h   10.244.7.185    c05                          <none>           <none>
```
- Exec into the flask deployment pod:
```
$ kubectl exec -it ngopal-final-flask-deployment-7dd864b899-5rrct -- /bin/bash
```
- Create 2 complaint/job entries using the following curl statements:
```
curl -X POST -H "content-type: application/json" -d '{"CASENUMBER": "1", "TYPEOFBUSINESS": "Bar", "TYPEOFCOMPLAINT": "Face Covering Non-Compliance", "OPENDATE": "2021-05-03", "CLOSEDATE": "2021-05-03", "OUTCOME": "No Violation(s) Found", "LONGITUDE": "-88.448709", "LATITUDE": "24.923983" }' 10.244.13.216:5000/create
```
```
{"JOBID": "f5a33325-4b01-4278-a3d8-245199db9864", "CASENUMBER": "1", "TYPEOFBUSINESS": "Bar", "TYPEOFCOMPLAINT": "Face Covering Non-Compliance", "OPENDATE": "2021-05-03", "CLOSEDATE": "2021-05-03", "OUTCOME": "No Violation(s) Found", "LATITUDE": "24.923983", "LONGITUDE": "-88.448709", "STATUS": "submitted"}
```
```
curl -X POST -H "content-type: application/json" -d '{"CASENUMBER": "2", "TYPEOFBUSINESS": "Restaurant", "TYPEOFCOMPLAINT": "Social Distancing", "OPENDATE": "2021-05-03", "CLOSEDATE": "2021-05-03", "OUTCOME": "Citation Issued", "LONGITUDE": "-88.448709", "LATITUDE": "24.923983" }' 10.244.13.216:5000/create
```
```
{"JOBID": "ddcf96cb-612a-4dcb-bc45-d752ef5b550c", "CASENUMBER": "2", "TYPEOFBUSINESS": "Restaurant", "TYPEOFCOMPLAINT": "Social Distancing", "OPENDATE": "2021-05-03", "CLOSEDATE": "2021-05-03", "OUTCOME": "Citation Issued", "LATITUDE": "24.923983", "LONGITUDE": "-88.448709", "STATUS": "submitted"}
```
- To display all CRUD job entries, use the following curl statement:
```
curl 10.244.13.216:5000/jobsubmits
```
```
|    |   CASENUMBER | CLOSEDATE   | JOBID                                |   LATITUDE |   LONGITUDE | OPENDATE   | OUTCOME               | STATUS      | TYPEOFBUSINESS   | TYPEOFCOMPLAINT              |
|---:|-------------:|:------------|:-------------------------------------|-----------:|------------:|:-----------|:----------------------|:------------|:-----------------|:-----------------------------|
|  0 |            2 | 2021-05-03  | ddcf96cb-612a-4dcb-bc45-d752ef5b550c |     24.924 |    -88.4487 | 2021-05-03 | Citation Issued       | in progress | Restaurant       | Social Distancing            |
|  1 |            1 | 2021-05-03  | f5a33325-4b01-4278-a3d8-245199db9864 |     24.924 |    -88.4487 | 2021-05-03 | No Violation(s) Found | in progress | Bar              | Face Covering Non-Compliance |
```
- Delete one of the complaint/job entries using the following curl statement:
```
curl 10.244.13.216:5000/delete?jobid=4c65cd0f-5684-42ce-80d9-b23f757caebb
```
```
Deleted complaint! (CASENUMBER: 2, JOBID: 4c65cd0f-5684-42ce-80d9-b23f757caebb)
```
```
curl 10.244.13.216:5000/jobsubmits
```
```
|    |   CASENUMBER | CLOSEDATE   | JOBID                                |   LATITUDE |   LONGITUDE | OPENDATE   | OUTCOME               | STATUS      | TYPEOFBUSINESS   | TYPEOFCOMPLAINT              |
|---:|-------------:|:------------|:-------------------------------------|-----------:|------------:|:-----------|:----------------------|:------------|:-----------------|:-----------------------------|
|  0 |            1 | 2021-05-03  | f5a33325-4b01-4278-a3d8-245199db9864 |     24.924 |    -88.4487 | 2021-05-03 | No Violation(s) Found | in progress | Bar              | Face Covering Non-Compliance |
```
- Download a graph analysis job using the following curl statement:
```
curl 10.244.13.216:5000/download/f5a33325-4b01-4278-a3d8-245199db9864 > output.png
```
```
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 19898    0 19898    0     0  1387k      0 --:--:-- --:--:-- --:--:-- 1387k
```
```
ls
```
```
output.png
```
