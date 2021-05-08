from jobs import q, rd, update_job_status
import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import redis

rd = redis.StrictRedis(host='172.17.0.1', port=6379, db=0)

@q.worker
def execute_job(jobid):
    update_job_status(jobid, 'in progress')
    time.sleep(15)

    df = pd.read_csv("./Austin_COVID-19_Complaint_Cases.csv")

    def df_query(x):
        return lambda dfx: dfx['TYPEOFCOMPLAINT'] == x

    # complaints related to face masks
    df1 = valid_df[df_query('Face Covering Non-Compliance - Business')]
    df2 = valid_df[df_query('Face Covering')]
    df3 = valid_df[df_query('Face-Covering')]
    # complaints related to social distancing
    df4 = valid_df[df_query('Social Distancing')]
    df5 = valid_df[df_query('Over Occupancy')]
    # complaints related to eviction
    df6 = valid_df[df_query('Eviction')]
    # complaints of other categories
    df7 = valid_df[df_query('Other')]

    plt.figure(figsize=(10,10))

    plt.scatter(df1.LATITUDE, df1.LONGITUDE, 1.0, 'b')
    plt.scatter(df2.LATITUDE, df2.LONGITUDE, 1.0, 'b')
    plt.scatter(df3.LATITUDE, df3.LONGITUDE, 1.0, 'b')
    plt.scatter(df4.LATITUDE, df4.LONGITUDE, 1.0, 'r')
    plt.scatter(df5.LATITUDE, df5.LONGITUDE, 1.0, 'r')
    plt.scatter(df6.LATITUDE, df6.LONGITUDE, 1.0, 'g')
    plt.scatter(df7.LATITUDE, df7.LONGITUDE, 1.0, 'y')

    plt.savefig('Austin_COVID_Complaints_Mapped.png')

    file_bytes = open('/tmp/Austin_COVID_Complaints_Mapped.png', 'rb').read()

    # set the file bytes as a key in Redis
    rd.set('key', file_bytes)

    update_job_status(jobid, 'complete')

execute_job()
