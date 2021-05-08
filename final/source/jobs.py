import uuid
from hotqueue import HotQueue
import redis
import os
import requests
import json
import pandas as pd
from datetime import datetime

q = HotQueue("queue", host='10.97.252.127', port=6379, db=1)
rd = redis.StrictRedis(host='10.97.252.127', port=6379, db=0)

def _generate_jid():
    return str(uuid.uuid4())

def _generate_job_key(jobid):
    if type(jobid) == bytes:
        jobid = jobid.decode('utf-8')
    return 'job.{}'.format(jobid)

def _instantiate_job(jobid, casenumber, typeofbusiness, typeofcomplaint, opendate, closedate, outcome, latitude, longitude, status):
    if type(jobid) == str:
        return {'JOBID':jobid,
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
    return {'JOBID':jobid.decode('utf-8'),
            'CASENUMBER':casenumber.decode('utf-8'),
            'TYPEOFBUSINESS':typeofbusiness.decode('utf-8'),
            'TYPEOFCOMPLAINT':typeofcomplaint.decode('utf-8'),
            'OPENDATE':opendate.decode('utf-8'),
            'CLOSEDATE':closedate.decode('utf-8'),
            'OUTCOME':outcome.decode('utf-8'),
            'LATITUDE': latitude.decode('utf-8'),
            'LONGITUDE': longitude.decode('utf-8'),
            'STATUS': status.decode('utf-8')
    }

def _save_job(job_key, job_dict):
    """Save a job object in the Redis database."""
    rd.hmset(job_key, job_dict)

def _queue_job(jobid):
    """Add a job to the redis queue."""
    q.put(jobid)

def add_job(casenumber, typeofbusiness, typeofcomplaint, opendate, closedate, outcome, latitude, longitude, status="submitted"):
    """Add a job to the redis queue."""
    jobid = _generate_jid()
    job_dict = _instantiate_job(jobid, casenumber, typeofbusiness, typeofcomplaint, opendate, closedate, outcome, latitude, longitude, status)
    # update call to save_job:
    _save_job(_generate_job_key(jobid), job_dict)
    # update call to queue_job:
    _queue_job(jobid)
    return job_dict

def update_job_status(jobid, new_status):
    """Update the status of job with job id `jid` to status `status`."""
    jobid, casenumber, typeofbusiness, typeofcomplaint, opendate, closedate, outcome, latitude, longitude, status = rd.hmget(_generate_job_key(jobid), 'JOBID', 'CASENUMBER', 'TYPEOFBUSINESS', 'TYPEOFCOMPLAINT',\
 'OPENDATE', 'CLOSEDATE', 'OUTCOME', 'LATITUDE', 'LONGITUDE', 'STATUS')
    job = _instantiate_job(jobid, casenumber, typeofbusiness, typeofcomplaint, opendate, closedate, outcome, latitude, longitude, status)

    if(new_status == 'in progress'):
        worker_IP = os.environ.get('WORKER_IP')
        print(worker_IP)
        rd.hset(_generate_job_key(jobid), 'worker', worker_IP)

    if job:
        job['STATUS'] = new_status
        _save_job(_generate_job_key(job['JOBID']), job)
    else:
        raise Exception()
