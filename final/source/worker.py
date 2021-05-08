from jobs import q, rd, update_job_status
import time
import redis

@q.worker
def execute_job(jobid):
    update_job_status(jobid, 'in progress')
    time.sleep(15)
    update_job_status(jobid, 'complete')

execute_job()
