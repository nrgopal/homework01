import json
from flask import Flask, request, send_file
import jobs
import requests
import pandas as pd
import redis
import os

app = Flask(__name__)

rd = redis.StrictRedis(host='10.97.252.127', port=6379, db=0)

@app.route('/create', methods=['POST'])
def create_jobs():
    try:
        job = request.get_json(force=True)
    except Exception as e:
        return True, json.dumps({'status': "Error", 'message': 'Invalid JSON: {}.'.format(e)})
    return json.dumps(jobs.add_job(job['CASENUMBER'], job['TYPEOFBUSINESS'], job['TYPEOFCOMPLAINT'], job['OPENDATE'], job['CLOSEDATE'], job['OUTCOME'], job['LATITUDE'], job['LONGITUDE']))

@app.route('/jobsubmits', methods=['GET'])
def get_jobs():

    jobs_dframe = pd.DataFrame()
    
    for key in rd.keys():
        jobid = (rd.hget(key, 'JOBID')).decode('utf-8')
        casenumber = (rd.hget(key, 'CASENUMBER')).decode('utf-8')
        typeofbusiness = (rd.hget(key, 'TYPEOFBUSINESS')).decode('utf-8')
        typeofcomplaint = (rd.hget(key, 'TYPEOFCOMPLAINT')).decode('utf-8')
        opendate = (rd.hget(key, 'OPENDATE')).decode('utf-8')
        closedate = (rd.hget(key, 'CLOSEDATE')).decode('utf-8')
        outcome = (rd.hget(key, 'OUTCOME')).decode('utf-8')
        latitude = (rd.hget(key, 'LATITUDE')).decode('utf-8')
        longitude = (rd.hget(key, 'LONGITUDE')).decode('utf-8')
        status = (rd.hget(key, 'STATUS')).decode('utf-8')

        next_job = {'JOBID':jobid,
                    'CASENUMBER':casenumber,
                    'TYPEOFBUSINESS':typeofbusiness,
                    'TYPEOFCOMPLAINT':typeofcomplaint,
                    'OPENDATE':opendate,
                    'CLOSEDATE':closedate,
                    'OUTCOME':outcome,
                    'LATITUDE': latitude,
                    'LONGITUDE': longitude,
                    'STATUS': status
        }

        jobs_dframe = jobs_dframe.append(next_job, ignore_index = True)

    return jobs_dframe.to_markdown()

@app.route('/delete', methods=['GET'])
def delete_job():
    jobid = request.args.get('jobid')

    for key in rd.keys():
        if jobid == (rd.hget(key, 'JOBID')).decode('utf-8'):
            casenumber = (rd.hget(key, 'CASENUMBER')).decode('utf-8')

    rd.delete(jobs._generate_job_key(jobid))
    return 'Deleted complaint! (CASENUMBER: ' + casenumber + ', JOBID: ' + jobid + ')'

@app.route('/download/<jobid>', methods=['GET'])
def download(jobid):
    path = f'/app/{jobid}.png'
    with open(path, 'wb') as f:
        f.write(rd.hget(jobid, 'image'))
    return send_file(path, mimetype='image/png', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
