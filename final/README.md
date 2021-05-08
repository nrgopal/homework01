# FINAL

The final project consists of building a REST API frontend to a time series database that allows for basic CRUD - Create, Read, Update, Delete - operations and also allows users to submit an analysis job of building a graph from the dataset.

This project is based on the dataset Austin Code COVID-19 Cases. 
The dataset can be found here: https://data.austintexas.gov/Public-Safety/Austin-Code-COVID-19-Complaint-Cases-Dashboard/5bvq-24pm

This dataset displays information on COVID-19 complaints which Austin Code has received since December 1st, 2020. This dataset is unique to Austin Code case responses and doesn't include case data from Austin Fire, Austin Police, or other entities responding to COVID-19 complaints.

Each entry in the dataset represents an individual complaint.

The project includes two separate pieces of documentation (located in final/docs): 
- DEPLOYMENT.md provides instructions for deploying the system
- DEVELOPER.md is geared towards users/developers who interact with the system

## A
Front-end API - A set of synchronous API endpoints providing the following functionality:
- Route to create new data points
- Route to delete data points
- Route to retrieve endpoints and return active job submission
- Graph submission and retrieval points

B.
Back-end workers - Backend/worker processes to work the submitted jobs:
- Worker processes framework.
- Analysis job: 
Using the Latitude and Longitude of each complaint, a scatterplot is generated to show a map of all case locations, color coded by complaint types. Refer to final/source/output.png and final/source/worker.py for details of the analysis.

C.
Use of Redis database and queue structures to link front-end and back-end processes.
