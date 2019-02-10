# DEEPSus

Davis Environmental & Energy Platform for Sustainability. [Devpost link here](https://devpost.com/software/deepsus)

## Overview

Real time data analytics from OSI PI system on UC Davis campus. Anomaly detection etc

![alt text](davis.png)

## System design

Design starts from the top down. We realized that before designing a system or "hack", we needed a real world problem to solve, and using data driven methodologies, sought to find a problem to tackle using OSIsoft PI's public API for UC Davis campus data. Initially, we used standard data analysis on a Jupyter notebook to discover the OSIsoft PI API and query data using its python client to identify key coorelations based on historical data that has already been pre-collected. In this step, we also thought of ways to automate and extend a system to gain more insight.

In designing our system, we wanted to keep all of our infrastructure on GCP. This was an informed decision after considering a potential automated the data pipeline.
* Data fetched from OSIsoft PI onto UC Davis public REST API
* Data of interest fetched from public REST API using OSIsoft PI python client, aggregated, and some precomputation and cleaning done into GCS bucket. Data is fetched on a schedule on GCP Compute Engine instance, and data piped into GCS buckets by Cloud Storage FUSE adapter so data in GCS bucket is not stale.
* Data in bucket is available for three use cases
  * ExpressJS server for our ReactJS real time graphing front end
  * Learning and data analytics/ML workloads on GCP
  * Data made publicly available
  
## Install

A few key components in this repository:

In the root directory, run the following commands to install and start ExpressJS server on port 8080. ExpressJS server fetches data from Google Cloud Storage. This application is hosted on Google Cloud App Engine and load balanced across 3 nodes.

```bash
npm install; 
npm start;
```

In the `client/` directory, run the following commands to install and start ReactJS front end web application on port 3000. ReactJS web app queries ExpressJS application on GCP to get OSIsoft data. See HTTP GET for `/api/getARC`.

```bash
cd client/;
npm install; 
npm start;
```

In the `scraper/` directory, run the following commands to scrape OSIsoft data into GCS bucket. The scraper is run on GCP Compute Engine. The scraper runs using OSIsoft python client, and needs to be installed separately. See the `scraper/Python` fdirectory for the required install instructions.

```bash
cd scraper/;
python3 scraper.py
```
